from fastapi import FastAPI
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION


def get_application() -> FastAPI:
    from app.api.routes.api import app as api_router
    from app.api.routes import authentication
    from app.api.helpers.download import download_video_template
    from app.api.database.migrate.init_super_user import init_super_user

    download_video_template()
    init_super_user()

    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION, docs_url=None)
    print()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # application.add_event_handler("startup", create_start_app_handler(application))
    # application.add_event_handler("shutdown", create_stop_app_handler(application))

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
        return templates.TemplateResponse("index.html", {"request": request})

    return application


app = get_application()

if __name__ == "__main__":
    import uvicorn
    import os

    HOST = os.getenv("APP_HOST")
    PORT = os.getenv("APP_PORT")
    uvicorn.run(app, host=HOST, port=int(PORT))
