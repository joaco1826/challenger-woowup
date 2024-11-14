from mongoengine import connect
from app.constants.database import MongoConstants

API_VERSION = "v0.1"


def connect_db() -> None:
    """

    :return: connect mongodb
    """
    connect(
        host=MongoConstants.URI,
        uuidRepresentation="standard"
    )