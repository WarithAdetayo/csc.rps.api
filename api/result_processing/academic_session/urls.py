from django.urls import path

from api.result_processing.academic_session.views import AcademicSessionListCreateView

urlpatterns = [
    path('', AcademicSessionListCreateView.as_view(), name='academic-session-list-create'),
    path('<str:academic_session_id>/', AcademicSessionListCreateView.as_view(), name='academic-session-detail'),
]
