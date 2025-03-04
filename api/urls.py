from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-docs'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('auth/', include('api.system_administration.auth.urls')),

    path('accounts/', include('api.system_administration.csc_rps_user.urls')),

    path('academic-sessions/', include('api.result_processing.academic_session.urls')),
    path('levels/', include('api.result_processing.level.urls')),
    path('students/', include('api.result_processing.student.urls'))
]
