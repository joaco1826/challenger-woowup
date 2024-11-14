from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.constants.config import Config
from app.frameworks.database.mongo import connect_db
from app.frameworks.http.middleware import SentryMiddleware
from app.frameworks.monitoring.sentry import init_sentry
from app.adapters.controllers.meta import router as meta_router

init_sentry()

app = FastAPI(
    title=Config.APP_NAME,
    description="API for send email",
    version=Config.API_VERSION,
    redoc_url=Config.REDOC,
    docs_url=Config.SWAGGER_URL,
    debug=Config.DEBUG
)

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
