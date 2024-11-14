import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

from app.constants.config import Config


def init_sentry():
    sentry_sdk.init(
        dsn=Config.SENTRY_DSN,
        integrations=[FastApiIntegration()],
        traces_sample_rate=1.0,
        environment=Config.APP_ENV,
    )
