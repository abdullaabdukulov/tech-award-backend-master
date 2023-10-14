from common.exceptions import (
    JWTTokenInvalidOrExpired,
    NotAuthenticationCredentials,
    ObjectNotFound,
    UserCredentialsError,
)
from rest_framework.exceptions import ErrorDetail
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    if response is not None:
        customized_response = {}
        customized_response["errors"] = []
        data = response_data_handler(response.data)
        for key, value in data.items():
            error = {"field": key, "message": value}
            customized_response["errors"].append(error)
        response.data = customized_response
        print(response.data)
    return response


def response_data_handler(data):
    if isinstance(data, list):
        data = {"non_field_errors": data}
    detail = data.get("detail", None)
    if detail is not None:
        match detail.code.lower():
            case "not_authenticated":
                error_detail = ErrorDetail(NotAuthenticationCredentials.default_detail)
                error_detail.code = NotAuthenticationCredentials.default_code
            case "no_active_account":
                error_detail = ErrorDetail(UserCredentialsError.default_detail)
                error_detail.code = UserCredentialsError.default_code
            case "token_not_valid":
                error_detail = ErrorDetail(JWTTokenInvalidOrExpired.default_detail)
                error_detail.code = JWTTokenInvalidOrExpired.default_code
            case "not_found":
                error_detail = ErrorDetail(ObjectNotFound.default_detail)
                error_detail.code = ObjectNotFound.default_code
            case "credentials_error":
                error_detail = ErrorDetail(UserCredentialsError.default_detail)
                error_detail.code = UserCredentialsError.default_code
            case _:
                error_detail = ErrorDetail(detail)
                error_detail.code = detail.code
        data = {"non_field_errors": [error_detail]}
    return data
