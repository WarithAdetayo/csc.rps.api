"""Module for Validator functions
"""
import re
from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from commons.config.exceptions import MaximumFileSizeExceedError
from commons.utils.defaults import Regex, FileSizeLimit


def start_date_before_end_date(start_date: datetime, end_date: datetime):
    """Validates the start date is equal to or less than the end date
    """
    if start_date > end_date:
        raise ValidationError(_("Start date should be before end date"))
    return start_date, end_date


def is_valid_phone_number(phone_number):
    """Validates that a phone number if is in the right format"""
    codes = ['080', '090', '070', '081', '091']
    if len(phone_number) != 11:
        raise ValidationError(_("Phone number may be incorrect"))
    if phone_number[0:3] not in codes:
        raise ValidationError(_("Phone number appears to be incorrect"))
    return phone_number


def is_dob_legal(dob):
    """Validates that the date of birth is not less than 16 years"""
    min_date = datetime.now() - timedelta(days=16 * 365)
    if dob > min_date.date():
        raise ValidationError(_("You should be more than 18 years old"))
    return dob


def is_unibadan_student_email(email):
    """Validates that the email is of University of Ibadan's student"""
    domain = email[-14:]
    if domain != '@stu.ui.edu.ng':
        raise ValidationError(_("Try using your official school email"))
    return email


def has_multiple_words(text: str):
    """Validates that the text has multiple words,
    useful in checking if names has first and last name
    """
    token = text.strip().split()
    if len(token) == 1:
        raise ValidationError(_("Please enter full details"))
    return text


def is_valid_matric_number(matric):
    """Validates that the matric number is correct"""
    # check if DLC
    matric_number = matric
    if len(matric) > 6:
        matric_number = matric[1:]
        if matric[0] != 'E':
            raise ValidationError(_("Enter your matric number properly!"))
    if len(matric_number) != 6:
        raise ValidationError(_("This matric number looks incorrect!"))
    if not matric_number.strip().isnumeric():
        raise ValidationError(_("This doesn't look like a matric number!"))
    return matric


def is_not_future_year(year):
    now_year = datetime.today().year
    if year > now_year:
        raise ValidationError(_("Year can't be in the future!"))
    return year


def password_validator(password):
    """Validate user password
    Criteria
        1. Minimum length of 8 characters.
        2. At least one lowercase letter.
        3. At least one uppercase letter.
        4. At least one digit.
        5. At least one special character.
    """

    if len(password) < 8:
        raise ValidationError(_("Password must be at least 8 characters long"))

    if not re.search(r'[a-z]', password):
        raise ValidationError(_("Password must contain at least one lowercase letter"))

    if not re.search(r'[A-Z]', password):
        raise ValidationError(_("Password must contain at least one uppercase letter"))

    if not re.search(r'[0-9]', password):
        raise ValidationError(_("Password must contain at least one digit"))

    if not re.search(r'[!@#$%^&*()-_=+{};:,<.>]', password):
        raise ValidationError(_("Password must contain at least one special character"))

    return password


def is_ui_student_mail(email: str) -> bool:
    # Regular, dlc, postgraduate
    return Regex.EMAIL_HAS_UI_DOMAIN_REGEX.fullmatch(email) is not None


def student_email_validator(email):
    if not is_ui_student_mail(email):
        raise ValidationError(_('Email is not a valid University of Ibadan student email'))
    return email


def session_validator(session: str):
    mo = Regex.SESSION_REGEX.fullmatch(session)

    if mo is None:
        raise ValidationError('Session is not in the correct format (yyyy/yyyy) or is out of supported range')

    start, end = session.split('/')

    if int(end) - int(start) != 1:
        raise ValidationError('Session end year must exceed the start year by exactly one year')

    return session


def address_validator(address: str):
    mo = Regex.ADDRESS_REGEX.fullmatch(address)

    if mo is None:
        raise ValidationError('Address is not in the acceptable format (street name, city/area and state are required)')

    return address


def ng_phone_number_validator(number: str):
    if Regex.NG_PHONE_NUMBER_REGEX.fullmatch(number) is None:
        raise ValidationError('Phone number is not in a correct format')
    return number


def single_space_between_words_validator(text: str):
    if '  ' in text:
        raise ValidationError('A single must be between two words')
    return text


def profile_image_file_size_validator(value):
    filesize = value.size
    if filesize > FileSizeLimit.PROFILE_IMAGE_SIZE_LIMIT * 1024:
        raise MaximumFileSizeExceedError(f"Maximum file size is {FileSizeLimit.PROFILE_IMAGE_SIZE_LIMIT}KB")


def validate_matric_number_against_programme_type(programme_type, matric_number, exc):
    if programme_type.name == 'DLC':
        if matric_number[0].lower() != 'e':
            raise exc('First character in matric number must be an \'e\' or \'E\'')
        if len(matric_number) != 7:
            raise exc('Matric number must be exactly 7 characters')
        if not matric_number[1:].isdigit():
            raise exc('Matric number must contain only digits after the first character')
    elif programme_type.name in ('REGULAR', 'POSTGRADUATE'):
        if len(matric_number) != 6:
            raise exc('Matric number must be exactly 6 digits')
        if not matric_number.isdigit():
            raise exc('Matric number must contain only digits')
    else:
        raise exc('Invalid programme type')
