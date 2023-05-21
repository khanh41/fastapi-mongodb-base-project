"""Start Application."""
import os

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.responses import Response

from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from app.logger.logger import custom_logger

if PROJECT_NAME:
    from app.api.routes.api import app as api_router
    from app.api.routes import authentication
    from app.api.database.migrate.init_super_user import init_super_user


class LoggingMiddleware(BaseHTTPMiddleware):
    """Logging All API request."""

    async def set_body(self, request: Request):
        """Set body."""
        receive_ = await request._receive()

        async def receive():
            """Receive body."""
            return receive_

        request._receive = receive

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """Dispatch."""
        await self.set_body(request)

        # Log the request
        custom_logger.info("Received request: %s %s", request.method, request.url)
        custom_logger.debug("Request headers: %s", request.headers)
        custom_logger.debug("Request body: %s", await request.body())

        # Call the next middleware or route handler
        response = await call_next(request)

        # Log the response
        custom_logger.info("Response status code: %s", response.status_code)
        custom_logger.debug("Response headers: %s", response.headers)

        return response


def get_application() -> FastAPI:
    """Get application.

    Returns:
        FastAPI application.
    """
    init_super_user()

    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION, docs_url=None)
    application.add_middleware(LoggingMiddleware)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_middleware(GZipMiddleware, minimum_size=1000)
    application.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=API_PREFIX)
    application.include_router(authentication.router, tags=["Authentication"])

    application.mount("/static", StaticFiles(directory="app/frontend/static"), name="static")

    templates = Jinja2Templates(directory="app/frontend/templates")

    @application.get("/", tags=["UI"], response_class=HTMLResponse, deprecated=False)
    async def read_root(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})

    return application


app = get_application()

if __name__ == "__main__":
    HOST = os.getenv("APP_HOST")
    PORT = os.getenv("APP_PORT")
    uvicorn.run(app, host=HOST, port=int(PORT))
