import os
from dotenv import load_dotenv

load_dotenv()


class EmailConstants:
    SENDGRID_URL = os.getenv("SENDGRID_URL")
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
    MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
    MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
