from django.urls import path, include
from api.system_administration.views import GenerateTemplateView, UploadScoreSheetView, UploadHistoryView

urlpatterns = [
    path('auth/', include('api.system_administration.auth.urls')),
    path('accounts/', include('api.system_administration.csc_rps_user.urls')),
    path('generate-template/<str:session_id>/<str:course_id>/', GenerateTemplateView.as_view(), name='generate-template'),
    path('upload-scores/<str:session_id>/<str:course_id>/', UploadScoreSheetView.as_view(), name='upload-scores'),
    path('upload-history/', UploadHistoryView.as_view(), name='upload-history'),
]