from rest_framework.views import APIView

"""
response structure

{
    status_code : 200,
    errors {},
    data {}
}
"""


def custom_response(view):
    def inner(self, request, *args, **kwargs):
        response = super(view, self).dispatch(request, args, **kwargs)
        list_errors = []
        response_data = response.data
        data = dict(
            success=True,
            errors=list_errors,
            data={},
        )
        if response.exception:
            data["success"] = False
            errors = response_data.get("errors")
            for e in errors:
                field = e.get("field")
                message = e.get("message")
                try:
                    if isinstance(message, list):
                        message_ = message[0]
                    else:
                        message_ = message
                    error_data = {
                        "field": field,
                        "message": message_,
                        "code": message_.code.upper(),
                    }
                except Exception:
                    error_data = {
                        "field": field,
                        "message": message,
                    }
                list_errors.append(error_data)
            data["errors"] = list_errors
        else:
            data["data"] = response_data
        response.data = data

        return response

    assert issubclass(view, APIView), (
        "class %s must be subclass of APIView" % view.__class__
    )

    view.dispatch = inner
    return view
