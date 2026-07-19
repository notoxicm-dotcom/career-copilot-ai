"""Custom exceptions."""


class AppException(Exception):
    """Base application exception."""

    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class UnauthorizedException(AppException):
    """Unauthorized exception."""

    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, 401)


class ForbiddenException(AppException):
    """Forbidden exception."""

    def __init__(self, message: str = "Forbidden"):
        super().__init__(message, 403)


class NotFoundException(AppException):
    """Not found exception."""

    def __init__(self, message: str = "Not found"):
        super().__init__(message, 404)


class ConflictException(AppException):
    """Conflict exception."""

    def __init__(self, message: str = "Conflict"):
        super().__init__(message, 409)


class ValidationException(AppException):
    """Validation exception."""

    def __init__(self, message: str = "Validation error"):
        super().__init__(message, 422)
