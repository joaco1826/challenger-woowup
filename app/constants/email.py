import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()


class EmailConstants:
    SENDGRID_URL = os.getenv("SENDGRID_URL")
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
    MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
    MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")


class Recipients(str, Enum):
    """ Recipients allowed
    * juaco.1826@gmail.com\n
    * jforeroola@gmail.com
    """
    MAILGUN = os.getenv("MAILGUN_RECIPIENT")
    SENDGRID = os.getenv("SENDGRID_RECIPIENT")

    @staticmethod
    def values() -> list:
        return list(map(lambda e: e.value, Recipients))


class Providers(str, Enum):
    """ Providers available
    * MAILGUN\n
    * SENDGRID
    """
    MAILGUN = 'MAILGUN'
    SENDGRID = 'SENDGRID'

    @staticmethod
    def values() -> list:
        return list(map(lambda e: e.value, Providers))
