import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()


class MongoConstants:
    URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    EMAIL_COLLECTION = "emails"


class Status(str, Enum):
    """ Status to email
    * PENDING\n
    * SENT\n
    * FAILED
    """
    PENDING = 'PENDING'
    SENT = 'SENT'
    FAILED = 'FAILED'

    @staticmethod
    def values() -> list:
        return list(map(lambda e: e.value, Status))
