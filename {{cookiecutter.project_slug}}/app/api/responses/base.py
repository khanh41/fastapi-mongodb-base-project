from fastapi.responses import JSONResponse
from starlette import status


class BaseResponse:
    def __init__(self) -> None:
        self.base_response = {
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "",
            "data": None,
        }

    @staticmethod
    def success_response(message="API success", status_code=status.HTTP_200_OK):
        return JSONResponse(
            status_code=status_code,
            content={
                "status": "failed",
                "status_code": status_code,
                "message": message,
            })

    @staticmethod
    def error_response(message="API error", status_code=status.HTTP_400_BAD_REQUEST):
        return JSONResponse(
            status_code=status_code,
            content={
                "status": "failed",
                "status_code": status_code,
                "message": message,
            })


response = BaseResponse()
