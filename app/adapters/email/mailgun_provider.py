import httpx
from sentry_sdk import capture_exception
from app.adapters.email.email_provider import EmailProvider
from app.constants.email import EmailConstants, Providers
from app.core.entities.email import Email


class MailgunProvider(EmailProvider):
    MAILGUN_API_KEY = EmailConstants.MAILGUN_API_KEY
    MAILGUN_DOMAIN = EmailConstants.MAILGUN_DOMAIN

    async def send_email(self, email: Email) -> (bool, str):
        try:
            auth = ("api", self.MAILGUN_API_KEY)
            data = {
                "from": email.sender,
                "to": [email.recipient],
                "subject": email.subject,
                "html": email.body,
            }

            async with httpx.AsyncClient() as client:
                response = await client.post(self.MAILGUN_DOMAIN, auth=auth, data=data)
                return response.status_code in [200, 201, 202], Providers.MAILGUN.value
        except Exception as e:
            capture_exception(e)
            print(str(e))
