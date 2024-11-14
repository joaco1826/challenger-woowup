import pytest

from app.constants.database import Status
from app.constants.email import Providers
from app.core.entities.email import EmailCreate, Email
from app.core.use_cases.send_email import SendEmail
from app.adapters.database.email_repository import EmailRepository
from app.adapters.email.mailgun_provider import MailgunProvider
from app.models.email_model import EmailModel


@pytest.mark.asyncio
async def test_send_email_integration_success(mocker):
    email_data = EmailCreate(
        sender="sender@example.com",
        recipient="users@gmail.com",
        subject="Test Email",
        body="<p>This is a test email</p>"
    )

    mock_create_email = mocker.patch.object(EmailRepository, "create_email", return_value=Email)
    mock_update_email_status = mocker.patch.object(EmailRepository, "update_email_status", return_value=EmailModel)

    mock_mailgun = mocker.patch.object(MailgunProvider, "send_email", return_value=(True, Providers.MAILGUN.value))

    send_email_use_case = SendEmail()

    result = await send_email_use_case.execute(email_data)

    assert result.status == Status.SENT.value
    assert result.provider == Providers.MAILGUN.value
    mock_create_email.assert_called_once_with(email_data)
    mock_update_email_status.assert_called_once_with(result)
    mock_mailgun.assert_called_once()
