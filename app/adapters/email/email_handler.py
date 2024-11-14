from sentry_sdk import capture_exception

from app.adapters.email.email_provider import EmailProvider
from app.core.entities.email import Email


class EmailHandler:
    def __init__(self, providers: list[EmailProvider]):
        self.providers = providers

    async def send_email(self, email: Email) -> (bool, str):
        provider = ""
        for pvd in self.providers:
            try:
                success, provider = await pvd.send_email(email)
                if success:
                    return True, provider
            except Exception as e:
                capture_exception(e)
                print(f"Error with provider {pvd.__class__.__name__}: {e}")
        return False, provider
