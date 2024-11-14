import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()


class EmailConstants:
    SENDGRID_SENDER = os.getenv("SENDGRID_SENDER")
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
    MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
    MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
    MAILGUN_SENDER = os.getenv("MAILGUN_SENDER")
    MESSAGE_EMAIL_FAILED = "The email could not be sent."
    MESSAGE_EMAIL_SUCCESS = "Email processed successfully."


class Senders(str, Enum):
    """ Senders allowed
    * mailgun@sandbox066420485fa7479b9b9c15968b61dccf.mailgun.org\n
    * jforeroola@gmail.com
    """
    MAILGUN = os.getenv("MAILGUN_SENDER")
    SENDGRID = os.getenv("SENDGRID_SENDER")

    @staticmethod
    def values() -> list:
        return list(map(lambda e: e.value, Senders))


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
