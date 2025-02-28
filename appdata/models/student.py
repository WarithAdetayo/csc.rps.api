import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from appdata.models.abstract.a_model_audit_mixin import AModelAuditMixin
from appdata.models.enums.choices import ModeOfEntry, Gender
from commons.utils.validators import session_validator, student_email_validator


class Student(AModelAuditMixin):

    student_id = models.CharField(verbose_name=_('Student Id'),
                                  primary_key=True,
                                  default=uuid.uuid4,
                                  max_length=64)

    matric_number = models.CharField(verbose_name=_('Matric Number'),
                                     max_length=64,
                                     unique=True,
                                     null=False, blank=False)

    first_name = models.CharField(verbose_name=_("First name"),
                                  max_length=255,
                                  null=False,
                                  blank=False)

    surname = models.CharField(verbose_name=_("Surname"),
                               max_length=255,
                               null=False,
                               blank=False)

    middle_name = models.CharField(verbose_name=_("Middle name"),
                                   max_length=255,
                                   null=True,
                                   blank=True)

    session_of_entry = models.CharField(verbose_name=_('Entry Session into Department'),
                                        max_length=16,
                                        blank=False,
                                        null=False,
                                        validators=[session_validator],
                                        help_text=_('Entry Session into Department'))

    year_of_admission = models.PositiveIntegerField(verbose_name=_('Year of Admission'),
                                                    blank=False,
                                                    null=False,
                                                    help_text=_('Year of Admission'))

    mode_of_entry = models.CharField(verbose_name=_('Mode of Entry'),
                                     null=False,
                                     blank=False,
                                     max_length=16,
                                     choices=ModeOfEntry.mapping())

    dob = models.DateField(verbose_name=_("Date of Birth"),
                           help_text=_('Date of Birth'))

    gender = models.CharField(_("Gender"),
                              max_length=6,
                              null=False,
                              blank=False,
                              help_text=_('Male or Female (we want only sane people here)'),
                              choices=Gender.mapping())

    school_email = models.EmailField(_("Student Email Address"),
                                     null=True,
                                     blank=True,
                                     validators=[student_email_validator])

    class Meta:
        verbose_name = _("Student Profile")
        verbose_name_plural = _("Student Profiles")
        db_table = "student"
