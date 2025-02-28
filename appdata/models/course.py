import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from appdata.models.abstract.a_model_audit_mixin import AModelAuditMixin
from appdata.models.level import Level


class Course(AModelAuditMixin):

    course_id = models.CharField(verbose_name=_('Course Id'),
                                 primary_key=True,
                                 default=uuid.uuid4,
                                 max_length=64)

    course_code = models.CharField(verbose_name=_('Course Code'),
                                   null=False,
                                   blank=False,
                                   max_length=8,
                                   unique=True)

    course_title = models.CharField(verbose_name=_('Course Title'),
                                    null=False,
                                    blank=False,
                                    max_length=512)

    course_unit = models.PositiveSmallIntegerField(verbose_name=_('Course Unit'),
                                                   null=False,
                                                   blank=False)

    level = models.ForeignKey(to=Level,
                              verbose_name=_('Level'),
                              on_delete=models.RESTRICT,
                              null=False,
                              blank=False)

    class Meta:
        verbose_name = _('Department Course')
        verbose_name_plural = _('Department Courses')
        db_table = 'course'

    def __str__(self):
        return f"{self.course_code}"
