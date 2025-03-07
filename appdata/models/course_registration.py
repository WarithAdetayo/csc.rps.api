from django.db import models
from appdata.models.abstract.a_model_audit_mixin import AModelAuditMixin
import uuid
from appdata.models.session_registration import SessionRegistration  # Added
from appdata.models.course import Course 

class CourseRegistration(AModelAuditMixin, models.Model):
    course_registration_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session_registration = models.ForeignKey(SessionRegistration, on_delete=models.CASCADE, related_name='course_registrations')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    ca_score = models.FloatField(null=True, blank=True)
    exam_score = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'course_registration'
        unique_together = ('session_registration', 'course')

    def __str__(self):
        return f"{self.session_registration.student} - {self.course.course_code}"