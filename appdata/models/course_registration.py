import uuid

from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _

from appdata.models.abstract.a_model_audit_mixin import AModelAuditMixin
from appdata.models.course import Course
from appdata.models.session_registration import SessionRegistration


class CourseRegistration(AModelAuditMixin):

    course_registration_id = models.CharField(verbose_name=_('Course Registration Id'),
                                              primary_key=True,
                                              default=uuid.uuid4,
                                              max_length=64)

    session_registration = models.ForeignKey(to=SessionRegistration,
                                             verbose_name=_('Session Registration'),
                                             blank=False,
                                             null=False,
                                             help_text=_('Session Registration'),
                                             on_delete=models.RESTRICT)

    course = models.ForeignKey(to=Course,
                               verbose_name=_('Course'),
                               blank=False,
                               null=False,
                               help_text=_('Course'),
                               on_delete=models.RESTRICT)

    score = models.PositiveSmallIntegerField(verbose_name=_('Score'),
                                             blank=True,
                                             null=True)

    class Meta:
        verbose_name = _('Course Registration')
        verbose_name_plural = _('Course Registrations')
        db_table = 'course_registration'

        constraints = [
            UniqueConstraint(fields=['session_registration', 'course'],
                             name='unique_course_registration',
                             violation_error_message='A course can only be registered once per student session '
                                                     'registration')
        ]

    def __str__(self):
        return (f"CourseRegistration<registration='{self.session_registration}', "
                f"score='{self.score}', course='{self.course}'>")
