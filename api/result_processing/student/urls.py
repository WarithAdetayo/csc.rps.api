from django.urls import path

from api.result_processing.student.views import StudentListCreateView, StudentDetailView

urlpatterns = [
    path('', StudentListCreateView.as_view(), name='student-list-create'),
    path('<str:student_id>/', StudentDetailView.as_view(), name='student-detail'),
]
