from datetime import datetime

from sentry_sdk import capture_exception

from app.adapters.email.email_handler import EmailHandler
from app.adapters.email.sendgrid_provider import SendGridProvider
from app.adapters.email.mailgun_provider import MailgunProvider
from app.adapters.database.email_repository import EmailRepository
from app.constants.database import Status
from app.constants.email import Senders
from app.core.entities.email import Email, EmailCreate


class SendEmail:
    def __init__(self):
        self.email_handler = EmailHandler(providers=[
            MailgunProvider(),
            SendGridProvider()
        ])
        self.email_repository = EmailRepository()

    async def execute(self, email_data: EmailCreate) -> Email:
        email = await self.email_repository.create_email(email_data)

        try:
            success, provider = await self.email_handler.send_email(email)
            email.provider = provider
            if success:
                email.status = Status.SENT.value
                email.sender = getattr(Senders, provider).value
                email.sent_at = datetime.utcnow()
            else:
                email.status = Status.FAILED.value
        except Exception as e:
            capture_exception(e)
            email.status = Status.FAILED.value
            print(f"Error sending email: {e}")
        finally:
            await self.email_repository.update_email_status(email)

        return email
