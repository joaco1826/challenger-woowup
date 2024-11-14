from datetime import datetime

from sentry_sdk import capture_exception

from app.adapters.email.email_handler import EmailHandler
from app.adapters.email.sendgrid_provider import SendGridProvider
from app.adapters.email.mailgun_provider import MailgunProvider
from app.adapters.database.email_repository import EmailRepository
from app.core.entities.email import Email, EmailBase


class SendEmail:
    def __init__(self):
        self.email_handler = EmailHandler(providers=[
            MailgunProvider(),
            SendGridProvider()
        ])
        self.email_repository = EmailRepository()

    async def execute(self, email_data: EmailBase) -> Email:
        email = await self.email_repository.create_email(email_data)

        try:
            success, provider = await self.email_handler.send_email(email)
            email.provider = provider
            if success:
                email.status = "sent"
                email.sent_at = datetime.utcnow()
            else:
                email.status = "failed"
        except Exception as e:
            capture_exception(e)
            email.status = "failed"
            print(f"Error sending email: {e}")
        finally:
            await self.email_repository.update_email_status(email)

        return email
