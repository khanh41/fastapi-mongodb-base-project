"""HTTP Error handler"""

from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def http_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """HTTP Error handler.

    Args:
        request: Request.
        exc: Exception.

    Returns:
        Json response error.
    """
    if request:
        pass

    return JSONResponse({"errors": [exc.detail]}, status_code=exc.status_code)
