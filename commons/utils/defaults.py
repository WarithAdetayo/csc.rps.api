"""The module define default values or constants"""
import re

DEFAULT_COUNTRY = 'Nigeria'


class FileSizeLimit:
    PROFILE_IMAGE_SIZE_LIMIT = 800  # 800 KB


class Regex:

    REGULAR_STUDENT_EMAIL_REGEX = re.compile("[a-z-]*\\d{3}@stu.ui.edu.ng")

    DLC_STUDENT_EMAIL_REGEX = re.compile("[eE]\\d{6}.\\w+@dlc.ui.edu.ng")

    EMAIL_HAS_UI_DOMAIN_REGEX = re.compile("\\w[\\w.-]+@[a-z]+.ui.edu.ng")

    NG_PHONE_NUMBER_REGEX = re.compile("(?:\\+234|0)\\d{10}")

    GLOBAL_PHONE_NUMBER_REGEX = re.compile("\\+\\d{3}\\d+")

    # 1948/1949 - 2999/3000  Support for 1,052 years (Crazy right? LOL)
    SESSION_REGEX = re.compile("(194[8-9]|19[5-9]\\d|2\\d{3})/(1949|19[5-9]\\d|2\\d{3}|3000)")

    # Format:
    #     123 Main Street, Anytown, State 12345, United States
    #
    # {Building Number} {Street name}, {Area}, {City}, {State} {Postal Code}, {Country}
    #
    # Building number     : (\\d[\\w]*)? (A number optionally followed by any word e.g 5, 89A, 345b)
    # Street name         : ([A-Z][\\w\\s-]+)
    # Area                : ([A-Z][\\w\\s-]+)?
    # City                : ([A-Z][a-z]+)
    # State               : ([A-Z][a-z]+)
    # Postal Code         : (\\d{5,})?
    # Country             : ([A-Z][\\w\\s]+)?
    ADDRESS_REGEX = re.compile("(?:(\\w+)\\s+)?([A-Z][\\w\\s-]+),\\s+(?:([A-Z][\\w\\s-]+),\\s)?([A-Z][a-z]+),\\s+([A-Z][a-z]+)(?:\\s+(\\d{5,}))?(?:,\\s+([A-Z][\\w\\s]+))?")
