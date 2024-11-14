from sentry_sdk import capture_exception
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from app.adapters.email.email_provider import EmailProvider
from app.constants.email import EmailConstants, Providers
from app.core.entities.email import Email


class SendGridProvider(EmailProvider):
    SENDGRID_API_KEY = EmailConstants.SENDGRID_API_KEY

    async def send_email(self, email: Email) -> (bool, str):
        message = Mail(
            from_email=email.recipient,
            to_emails=email.sender,
            subject=email.subject,
            html_content=email.body
        )
        try:
            sg = SendGridAPIClient(self.SENDGRID_API_KEY)
            response = sg.send(message)
            return response.status_code in [200, 201, 202], Providers.SENDGRID.value
        except Exception as e:
            capture_exception(e)
            print(str(e))
