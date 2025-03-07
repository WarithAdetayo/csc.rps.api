from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.system_administration.views import GenerateTemplateView, UploadScoreSheetView, UploadHistoryView

urlpatterns = [
    path('auth/', include('api.system_administration.auth.urls')),
    path('accounts/', include('api.system_administration.csc_rps_user.urls')),

    path('academic-sessions/', include('api.result_processing.academic_session.urls')),
    path('levels/', include('api.result_processing.level.urls')),
    path('students/', include('api.result_processing.student.urls')),
    path('session-registration/', include('api.result_processing.session_registration.urls'))
]
