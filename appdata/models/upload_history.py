import os
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from appdata.models.abstract.a_model_audit_mixin import AModelAuditMixin
from appdata.models.academic_session import AcademicSession
from appdata.models.course import Course
from commons.utils.file_utils import rename_file_with_current_timestamp


def upload_file(instance, filename):
    path = os.path.join(settings.SYSTEM_FILES_DIR_ROOT, 'uploads', rename_file_with_current_timestamp(filename))
    return path


class UploadHistory(AModelAuditMixin):
    upload_history_id = models.CharField(verbose_name=_('Upload History Id'),
                                         primary_key=True,
                                         default=uuid.uuid4,
                                         max_length=64)

    session = models.ForeignKey(to=AcademicSession,
                                verbose_name=_('Academic Registration'),
                                blank=False,
                                null=False,
                                help_text=_('Academic Registration'),
                                on_delete=models.RESTRICT)

    course = models.ForeignKey(to=Course,
                               verbose_name=_('Course'),
                               blank=False,
                               null=False,
                               help_text=_('Course'),
                               on_delete=models.RESTRICT)

    upload_timestamp = models.DateTimeField(verbose_name=_('Upload Timestamp'),
                                            null=False,
                                            blank=False,
                                            default=timezone.now,
                                            editable=False)

    uploaded_file = models.FileField(upload_to=upload_file,
                                     null=False,
                                     blank=False)

    class Meta:
        verbose_name = _('Upload History')
        verbose_name_plural = _('Upload Histories')
        db_table = 'upload_history'

    def __str__(self):
        return f"UploadHistory<session='{self.session}', course='{self.course}'>"
