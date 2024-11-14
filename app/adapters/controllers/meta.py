from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from app.constants.config import Config

router = APIRouter()


@router.get("/", tags=["Meta"])
async def root():
    response = {
        "MicroService": Config.APP_NAME
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )


@router.get("/version", tags=["Meta"])
async def version():
    response = {
        "version": Config.API_VERSION,
        "MicroService": Config.APP_NAME
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )