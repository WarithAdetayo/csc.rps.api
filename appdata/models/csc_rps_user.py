import os
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from appdata.managers import CSCRPSUserManager


def upload_avatar(instance, filename):
    path = os.path.join(settings.USER_ACCOUNT_FILES_DIR_ROOT, 'avatar', filename)
    return path


class CSCRPSUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model of CSC RPS User account.
    Uses email for authentication and stores basic user information

    Attributes:
        email (string): User's email address
        date_joined (datetime): Date account was created
        is_active (bool): Is this user active? (Useful for disabling accounts)
        is_verified (bool): Is this user email verified?

    """
    user_id = models.CharField(verbose_name=_('User Id'),
                               max_length=64,
                               primary_key=True,
                               default=uuid.uuid4,
                               blank=True)

    email = models.EmailField(verbose_name=_("Email Address"),
                              unique=True,
                              max_length=255,
                              validators=[EmailValidator()])

    first_name = models.CharField(_("First Name"), max_length=150, blank=True)

    last_name = models.CharField(_("Last Name"), max_length=150, blank=True)

    is_staff = models.BooleanField(_("staff status"), default=False,
                                   help_text=_("Designates whether the user can log into this admin site."))

    date_joined = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    is_verified = models.BooleanField(default=False)

    profile_picture = models.ImageField(upload_to=upload_avatar,
                                        null=True,
                                        blank=True)

    objects = users = CSCRPSUserManager()
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _('CSC RPS User Account')
        verbose_name_plural = _('CSC RPS User Accounts')
        db_table = 'csc_rps_user'

    def __str__(self):
        return f"CSCRPSUser<{self.email}>"
