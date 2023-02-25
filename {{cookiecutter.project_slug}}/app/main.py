"""Config and run application."""
import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION

if PROJECT_NAME:
    from app.api.database.migrate.init_super_user import init_super_user
    from app.api.routes import authentication
    from app.api.routes.api import app as api_router
else:
    raise ImportError("Wrong import order")


def get_application() -> FastAPI:
    """Define application config."""
    init_super_user()

    application = FastAPI(
        title=PROJECT_NAME, debug=DEBUG, version=VERSION, docs_url=None
    )
    print()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=API_PREFIX)
    application.include_router(authentication.router, tags=["Authentication"])

    application.mount(
        "/static", StaticFiles(directory="app/frontend/static"), name="static"
    )

    templates = Jinja2Templates(directory="app/frontend/templates")

    @application.get("/", tags=["UI"], response_class=HTMLResponse, deprecated=False)
    async def read_root(request: Request):
        """Template Response UI."""
        return templates.TemplateResponse("index.html", {"request": request})

    return application


app = get_application()

if __name__ == "__main__":
    HOST = os.getenv("APP_HOST")
    PORT = os.getenv("APP_PORT")
    uvicorn.run(app, host=HOST, port=int(PORT))
