import threading

from django.contrib.auth.models import AnonymousUser

_request = threading.local()
_context_user = threading.local()


class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Store the request in the thread-local variable
        _request.value = request
        response = self.get_response(request)
        return response


class ContextUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _context_user.value = request.user
        response = self.get_response(request)
        return response


def get_current_request():
    """Retrieve the current request from thread-local storage."""
    return getattr(_request, 'value', None)


def get_context_user():
    """
    Returns the current user from the thread local storage.
    Returns AnonymousUser if no user is set.
    """
    return getattr(_context_user, 'value', AnonymousUser())
