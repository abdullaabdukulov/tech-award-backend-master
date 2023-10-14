from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import (
    AuthenticationFailed,
    NotAuthenticated,
    NotFound,
    PermissionDenied,
    ValidationError,
)


class UserCredentialsError(AuthenticationFailed):
    default_detail = _("The provided credentials do not match our records.")
    default_code = "CREDENTIALS_ERROR"


# Dashboard exceptions
class AccessDenided(PermissionDenied):
    default_detail = _(
        "Oops, sorry! Something is wrong with your account. Contact the administrator."  # noqa
    )
    default_code = "ACCESS_DENIDED"


class UsernameAlreadyExists(ValidationError):
    default_detail = _("This username is linked to another account.")
    default_code = "USERNAME_ALREADY_EXISTS"


class AttributeUniqueError(ValidationError):
    default_detail = _("This attribute must be unique.")
    default_code = "ATTRIBUTE_UNIQUE_ERROR"


class MainImageAlreadyExists(ValidationError):
    default_detail = _("Main image already exists.")
    default_code = "MAIN_IMAGE_ALREADY_EXISTS"


class ProductAlredyExists(ValidationError):
    default_detail = _("Product is already exists in the store.")
    default_code = "PRODUCT_ALREADY_EXISTS"


class ProductNotFound(NotFound):
    default_detail = _("Product not found in the store.")
    default_code = "PRODUCT_NOT_FOUND"


# Application exceptions


class CodeResendError(ValidationError):
    default_detail = (
        "Verification code has already been sent. Wait for a timer to finish."  # noqa
    )
    default_code = "CODE_RESEND_ERROR"


class UserNotFound(NotFound):
    default_detail = _("User not found.")
    default_code = "USER_NOT_FOUND"


class ObjectNotFound(NotFound):
    default_detail = _("Not found.")
    default_code = "NOT_FOUND"


class PhoneNumberAlreadyExists(ValidationError):
    default_detail = _("This phone number is linked to another account.")
    default_code = "PHONE_NUMBER_ALREADY_EXISTS"


class PhoneNumberNotFound(NotFound):
    default_detail = _("Phone number is not linked to the account.")
    default_code = "PHONE_NUMBER_NOT_FOUND"


class PhoneNumberNotVerified(ValidationError):
    default_detail = _("Your phone is not verified.")
    default_code = "PHONE_NUMBER_NOT_VERIFIED"


class CodeError(ValidationError):
    default_detail = _("Verification code must be 6 digits.")
    default_code = "VERIFICATION_CODE_ERROR"


class CodeExpiredOrInvalid(ValidationError):
    default_detail = _(" Verification code expired or invalid.")
    default_code = "VERIFICATION_CODE_EXPIRED_OR_INVALID"


class JWTTokenInvalidOrExpired(AuthenticationFailed):
    default_detail = _("Authorization has failed, Please send valid token.")
    default_code = "TOKEN_INVALID_OR_EXPIRED"


class JWTTokenExpired(AuthenticationFailed):
    default_detail = _("Authentication token has expired.")
    default_code = "TOKEN_EXPIRED"


class NotAuthenticationCredentials(NotAuthenticated):
    default_detail = _(
        "Authentication credentials were not provided, please send valid token in headers."  # noqa
    )
    default_code = "NOT_AUTHENTICATED"
