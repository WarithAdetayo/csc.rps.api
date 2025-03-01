from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError


# Generic Exceptions
class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


class InternalServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


class MaximumFileSizeExceedError(ValidationError):
    default_detail = _('Maximum file size exceeded')
    default_code = 'max_file_exceeded'


class NotSupportedError(RuntimeError):
    default_detail = _('Operation is Not supported')
    default_code = 'operation_not_supported'


class TokenValidationError(ValidationError):
    default_detail = _('Token is not valid')
    default_code = 'token_validation_error'
