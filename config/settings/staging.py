from .base import *  # noqa

ALLOWED_HOSTS = [
    "localhost",
    "api.staging.example.com",
    "127.0.0.1",
]
DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3011",
    "http://127.0.0.1:3011",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CSRF_TRUSTED_ORIGINS = [
    "https://api.staging.example.com",
    "http://localhost",
]

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "[Bearer {JWT}]": {
            "name": "Authorization",
            "type": "apiKey",
            "in": "header",
        }
    },
    "USE_SESSION_AUTH": False,
    # "APIS_SORTER": "alpha",
    "SUPPORTED_SUBMIT_METHODS": ["get", "post", "put", "delete", "patch"],
    # "OPERATIONS_SORTER": "alpha",
}
