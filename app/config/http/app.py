from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.constants.config import Config
from app.config.database.mongo import connect_db
from app.config.http.middleware import SentryMiddleware
from app.config.monitoring.sentry import init_sentry
from app.adapters.controllers.meta import router as meta_router
from app.adapters.controllers.email_controller import router as email_router

init_sentry()

app = FastAPI(
    title=Config.APP_NAME,
    description="API for send email",
    version=Config.API_VERSION,
    redoc_url=Config.REDOC,
    docs_url=Config.SWAGGER_URL,
    debug=Config.DEBUG
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("app/static/index.html") as f:
        return HTMLResponse(content=f.read())

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SentryMiddleware
)

app.add_event_handler(
    "startup",
    connect_db,
)

app.include_router(
    meta_router
)

app.include_router(
    email_router,
    prefix="/api/v1"
)
