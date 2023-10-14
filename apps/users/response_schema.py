from drf_yasg import openapi

from .serializers import StudentProfileSerializer

RESPONSE_SCHEMA_400 = "Bad Request"

RESPONSE_SCHEMA_DEFAULT = openapi.Response(
    description="Error",
    examples={
        "application/json": {"detail": "An error occurred."},
    },
)

STUDENT_REGISTER_EXAMPLE_RESPONSE = {
    "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
    "first_name": openapi.Schema(type=openapi.TYPE_STRING, example="John"),
    "last_name": openapi.Schema(type=openapi.TYPE_STRING, example="Doe"),
    "email": openapi.Schema(type=openapi.TYPE_STRING, example="johndoe@example.com"),
}

STUDENT_REGISTER_REQUEST_BODY_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "first_name": openapi.Schema(type=openapi.TYPE_STRING, example="John"),
        "last_name": openapi.Schema(type=openapi.TYPE_STRING, example="Doe"),
        "email": openapi.Schema(
            type=openapi.TYPE_STRING, example="johndoe@example.com"
        ),
        "password": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_PASSWORD,
            example="your_password",
        ),
    },
    required=["first_name", "last_name", "email", "password"],
)

STUDENT_REGISTER_RESPONSE_SCHEMA_201 = openapi.Response(
    description="Created",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties=STUDENT_REGISTER_EXAMPLE_RESPONSE,
    ),
)

login_schema = {
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "email": openapi.Schema(type=openapi.TYPE_STRING),
            "password": openapi.Schema(
                type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD
            ),
        },
    ),
    "responses": {
        200: openapi.Response(
            description="Login successful",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "access": openapi.Schema(type=openapi.TYPE_STRING),
                    "refresh": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        400: "Bad Request",
    },
}

STUDENT_PROFILE_RESPONSE = {
    200: openapi.Response(
        description="Success",
        content={"application/json": {"schema": StudentProfileSerializer}},
    )
}
