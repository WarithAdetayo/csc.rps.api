from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


@extend_schema(
    summary='Obtain access and refresh tokens',
    tags=['Authentication']
)
class ObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AllowAny]


@extend_schema(
    summary='Refresh access token',
    tags=['Authentication']
)
class RefreshTokenView(TokenRefreshView):
    permission_classes = [AllowAny]


@extend_schema(
    summary='Verify access token',
    tags=['Authentication']
)
class VerifyTokenView(TokenVerifyView):
    permission_classes = [AllowAny]
