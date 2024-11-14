from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from sentry_sdk import capture_exception

app = FastAPI()


class SentryMiddleware(BaseHTTPMiddleware):
    @app.middleware("http")
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:
            capture_exception(exc)
            return JSONResponse(
                content={"detail": "Internal Server Error"},
                status_code=500
            )
