"""Base Response."""

from fastapi.responses import JSONResponse, ORJSONResponse
from starlette import status


class BaseResponse:
    """Base Response."""

    @staticmethod
    def success_response(
        message: str = "SUCCESS",
        status_code: int = status.HTTP_200_OK,
        message_code: int = 0,
        data=None,
    ):
        """Success response with a message and status code."""
        if data is None:
            return JSONResponse(
                status_code=status_code,
                content={
                    "message_code": message_code,
                    "message": message,
                },
            )
        else:
            return ORJSONResponse(
                status_code=status_code,
                content={
                    "message_code": message_code,
                    "message": message,
                    "data": data,
                },
            )

    @staticmethod
    def error_response(message: str = "ERROR", status_code: int = status.HTTP_400_BAD_REQUEST, message_code: int = 0):
        """Error response with a message and status code."""
        return JSONResponse(
            status_code=status_code,
            content={
                "message_code": message_code,
                "message": message,
            }
        )
