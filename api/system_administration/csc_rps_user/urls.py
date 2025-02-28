from django.urls import path

from api.system_administration.csc_rps_user.views import CreateAccountAPIView, ChangeProfilePictureAPIView

urlpatterns = [
    path('', CreateAccountAPIView.as_view(), name='create-account'),
    path('profile-picture/', ChangeProfilePictureAPIView.as_view(), name='profile-picture')
]