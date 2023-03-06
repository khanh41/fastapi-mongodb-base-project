"""Validation Error."""
from __future__ import annotations

from fastapi.exceptions import RequestValidationError
from fastapi.openapi.constants import REF_PREFIX
from fastapi.openapi.utils import validation_error_response_definition
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


async def http422_error_handler(
        request: Request,
        exc: (RequestValidationError | ValidationError),
) -> JSONResponse:
    """HTTP 422 Error handler.

    Args:
        request: Request.
        exc: Exception.

    Returns:
        Json response 422 error.
    """
    if request:
        pass

    return JSONResponse(
        {"errors": exc.errors()},
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )


validation_error_response_definition["properties"] = {
    "errors": {
        "title": "Errors",
        "type": "array",
        "items": {"$ref": f"{REF_PREFIX}ValidationError"},
    },
}
