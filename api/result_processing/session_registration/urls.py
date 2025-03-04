from django.urls import path

from api.result_processing.session_registration.views import SessionRegistrationDetailView, \
    SessionRegistrationListCreateView

urlpatterns = [
    path('', SessionRegistrationListCreateView.as_view(), name='session-registration-list-create'),
    path('<str:session_registration_id>/', SessionRegistrationDetailView.as_view(), name='session-registration-detail'),
]
