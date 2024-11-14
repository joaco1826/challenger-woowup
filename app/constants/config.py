import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    APP_ENV = os.getenv("APP_ENV", "development")
    DEBUG = APP_ENV == "development"
    APP_NAME = os.getenv("APP_NAME", "Email service")
    SENTRY_DSN = os.getenv("SENTRY_DSN")
    API_VERSION = "0.0.1"
    SWAGGER_URL = "/swagger"
    REDOC = "/redoc"
