from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class BaseResponse:
    def __init__(self) -> None:
        self.base_response = {
            "status": "success",
            "status_code": HTTP_200_OK,
            "message": "",
            "data": None,
        }

    @staticmethod
    def success_response(message="API success", status=HTTP_200_OK):
        return {"status": "success", "status_code": status, "message": message}

    @staticmethod
    def error_response(message="API error", status=HTTP_400_BAD_REQUEST):
        return {
            "status": "failed",
            "status_code": status,
            "message": message,
        }
