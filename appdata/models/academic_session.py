import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from appdata.models.abstract.a_model_audit_mixin import AModelAuditMixin
from commons.utils.validators import session_validator


class AcademicSession(AModelAuditMixin):

    academic_session_id = models.CharField(verbose_name=_('Session Id'),
                                           primary_key=True,
                                           default=uuid.uuid4,
                                           max_length=64)

    session = models.CharField(verbose_name=_('Academic Session'),
                               max_length=16,
                               blank=False,
                               null=False,
                               validators=[session_validator],
                               help_text=_('Academic Session'))

    class Meta:
        verbose_name = _('Academic Session')
        verbose_name_plural = _('Academic Sessions')
        db_table = 'academic_session'

    def __str__(self):
        return f"{self.session}"
