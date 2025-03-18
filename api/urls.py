from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.system_administration.views import GenerateTemplateView, UploadScoreSheetView, UploadHistoryView

urlpatterns = [
    path('auth/', include('api.system_administration.auth.urls')),
    path('accounts/', include('api.system_administration.csc_rps_user.urls')),

    path('generate-template/<str:session_id>/<str:course_id>/', GenerateTemplateView.as_view(), name='generate-template'),
    path('upload-scores/<str:session_id>/<str:course_id>/', UploadScoreSheetView.as_view(), name='upload-scores'),
    path('upload-history/', UploadHistoryView.as_view(), name='upload-history'),

    #Jwt endpoints
    path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    
      path('academic-sessions/', include('api.result_processing.academic_session.urls')),
    path('levels/', include('api.result_processing.level.urls')),
    path('students/', include('api.result_processing.student.urls')),
    path('session-registration/', include('api.result_processing.session_registration.urls'))
]




