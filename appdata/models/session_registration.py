import uuid

from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _

from appdata.models.abstract.a_model_audit_mixin import AModelAuditMixin
from appdata.models.academic_session import AcademicSession
from appdata.models.level import Level
from appdata.models.student import Student


class SessionRegistration(AModelAuditMixin):

    session_registration = models.CharField(verbose_name=_('Session Registration Id'),
                                            primary_key=True,
                                            default=uuid.uuid4,
                                            max_length=64)

    session = models.ForeignKey(to=AcademicSession,
                                verbose_name=_('Academic Session'),
                                blank=False,
                                null=False,
                                help_text=_('Academic Session'),
                                on_delete=models.RESTRICT)

    student = models.ForeignKey(to=Student,
                                verbose_name=_('Student'),
                                blank=False,
                                null=False,
                                on_delete=models.RESTRICT)

    level = models.ForeignKey(to=Level,
                              verbose_name=_('Level'),
                              blank=False,
                              null=False,
                              on_delete=models.RESTRICT)

    class Meta:
        verbose_name = _('Session Registration')
        verbose_name_plural = _('Session Registrations')
        db_table = 'session_registration'

        constraints = [
            UniqueConstraint(fields=['session', 'student'],
                             name='unique_session_registration',
                             violation_error_message='Student can only have one registration per session')
        ]

    def __str__(self):
        return f"SessionRegistration<session='{self.session}', level='{self.level}', student='{self.student}'>"
