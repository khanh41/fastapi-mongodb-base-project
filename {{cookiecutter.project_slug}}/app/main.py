"""Start Application."""
import random
import string
import time

import hypercorn.trio
import trio
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response

from app.api.database.migrate.init_super_user import init_super_user
from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.api.routes import authentication
from app.api.routes.api import app as api_router
from app.core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from app.core.constant import APP_HOST, APP_PORT
from app.logger.logger import custom_logger


class LoggingMiddleware(BaseHTTPMiddleware):
    """Logging All API request."""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """Dispatch."""
        idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        custom_logger.info(f"rid={idem} start request {request.method} {request.url.path}")
        start_time = time.time()

        # Log the request
        custom_logger.info("Received request: %s %s", request.method, request.url)
        custom_logger.debug("Request headers: %s", request.headers)
        custom_logger.debug("Request body: %s", await request.body())

        # Call the next middleware or route handler
        response = await call_next(request)

        process_time = (time.time() - start_time) * 1000
        formatted_process_time = '{0:.2f}'.format(process_time)

        custom_logger.info(
            "rid=%s method=%s path=%s completed_in=%sms status_code=%s",
            idem, request.method, request.url.path, formatted_process_time, response.status_code,
        )
        custom_logger.info("Response status code: %s", response.status_code)
        custom_logger.debug("Response headers: %s", response.headers)

        return response


def get_application() -> FastAPI:
    """Get application."""
    init_super_user()

    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION, docs_url=None)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_middleware(LoggingMiddleware)
    # application.add_middleware(GZipMiddleware, minimum_size=1000)
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

    @application.get("/logger", response_class=HTMLResponse, deprecated=False)
    async def get_logger():
        with open("app/logger/logger.log", "r") as f:
            log_str = f.read()
            log_html = f"<pre>{log_str}</pre>"
            return log_html

    return application


async def app_handler(scope, receive, send):
    await app(scope, receive, send)


async def main():
    config = hypercorn.trio.Config.from_mapping(
        bind=[f"{APP_HOST}:{APP_PORT}"],
        workers=1,
    )
    await hypercorn.trio.serve(app_handler, config)


app = get_application()

if __name__ == "__main__":
    trio.run(main)
