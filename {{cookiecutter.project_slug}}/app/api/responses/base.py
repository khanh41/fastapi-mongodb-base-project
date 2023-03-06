"""Base Response."""

from fastapi.responses import JSONResponse
from starlette import status


class BaseResponse:
    """Base Response."""

    def __init__(self) -> None:
        """Init base response."""
        self.base_response = {
            "message_code": 0,
            "message": "",
            "data": None,
        }

    @staticmethod
    def success_response(message: str = "API success", status_code: int = status.HTTP_200_OK, message_code: int = 0):
        """Success response with message and status code.

        Args:
            message: API Message.
            status_code: API status code.
            message_code: API message code.

        Returns:
            Success response.
        """
        return JSONResponse(
            status_code=status_code,
            content={
                "message_code": message_code,
                "message": message,
            }
        )

    @staticmethod
    def error_response(message: str = "API error", status_code: int = status.HTTP_200_OK, message_code: int = 0):
        """Error response with message and status code.

        Args:
            message: API Message.
            status_code: API status code.
            message_code: API message code.

        Returns:
            Error response.
        """
        return JSONResponse(
            status_code=status_code,
            content={
                "message_code": message_code,
                "message": message,
            }
        )


response = BaseResponse()
