from datetime import datetime

import pytest
from unittest.mock import AsyncMock
from httpx import Response
from app.adapters.email.mailgun_provider import MailgunProvider
from app.constants.database import Status
from app.core.entities.email import Email
from app.constants.email import Providers, EmailConstants


@pytest.fixture
def mailgun_provider():
    return MailgunProvider()


@pytest.fixture
def mock_email():
    return Email(
        sender=EmailConstants.MAILGUN_SENDER,
        recipient="users@gmail.com",
        subject="Test Email",
        body="<p>This is a test email</p>",
        email_uuid="1234",
        status=Status.PENDING.value,
        created_at=datetime.utcnow(),
        provider=Providers.MAILGUN.value
    )


@pytest.mark.asyncio
async def test_send_email_success(mocker, mailgun_provider, mock_email):
    mock_post = mocker.patch("httpx.AsyncClient.post", new_callable=AsyncMock)
    mock_post.return_value = Response(status_code=200)

    success, provider = await mailgun_provider.send_email(mock_email)

    assert success is True
    assert provider == Providers.MAILGUN.value

    mock_post.assert_called_once_with(
        mailgun_provider.MAILGUN_DOMAIN,
        auth=("api", mailgun_provider.MAILGUN_API_KEY),
        data={
            "from": mock_email.sender,
            "to": [mock_email.recipient],
            "subject": mock_email.subject,
            "html": mock_email.body,
        },
    )


@pytest.mark.asyncio
async def test_send_email_failure(mocker, mailgun_provider, mock_email):
    mock_post = mocker.patch("httpx.AsyncClient.post", new_callable=AsyncMock)
    mock_post.return_value = Response(status_code=400)

    success, provider = await mailgun_provider.send_email(mock_email)

    assert success is False
    assert provider == Providers.MAILGUN.value
    mock_post.assert_called_once()
