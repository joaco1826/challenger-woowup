from datetime import datetime

import pytest
from unittest.mock import AsyncMock

from app.constants.database import Status
from app.constants.email import Providers
from app.core.entities.email import Email, EmailCreate
from app.core.use_cases.send_email import SendEmail


@pytest.fixture
def send_email_use_case():
    return SendEmail()


@pytest.fixture
def mock_email_create():
    return EmailCreate(
        recipient="users@gmail.com",
        subject="Test Email",
        body="This is a test email."
    )


@pytest.fixture
def mock_email():
    return Email(
        sender="jforeroola@gmail.com",
        recipient="users@gmail.com",
        subject="Test Email",
        body="<p>This is a test email</p>",
        email_uuid="1234",
        status=Status.PENDING.value,
        created_at=datetime.utcnow(),
        provider=Providers.MAILGUN.value
    )


@pytest.mark.asyncio
async def test_send_email_success(mocker, send_email_use_case, mock_email_create, mock_email):
    mock_create_email = mocker.patch.object(
        send_email_use_case.email_repository, "create_email", new_callable=AsyncMock
    )
    mock_create_email.return_value = mock_email

    mock_update_email_status = mocker.patch.object(
        send_email_use_case.email_repository, "update_email_status", new_callable=AsyncMock
    )

    mock_send_email = mocker.patch.object(
        send_email_use_case.email_handler, "send_email", new_callable=AsyncMock
    )
    mock_send_email.return_value = (True, Providers.SENDGRID.value)

    result = await send_email_use_case.execute(mock_email_create)

    assert result.status == Status.SENT.value
    assert result.provider == Providers.SENDGRID.value
    assert result.sent_at is not None
    mock_create_email.assert_called_once_with(mock_email_create)
    mock_send_email.assert_called_once_with(mock_email)
    mock_update_email_status.assert_called_once_with(result)


@pytest.mark.asyncio
async def test_send_email_failure(mocker, send_email_use_case, mock_email_create, mock_email):
    mock_create_email = mocker.patch.object(
        send_email_use_case.email_repository, "create_email", new_callable=AsyncMock
    )
    mock_create_email.return_value = mock_email

    mock_update_email_status = mocker.patch.object(
        send_email_use_case.email_repository, "update_email_status", new_callable=AsyncMock
    )

    mock_send_email = mocker.patch.object(
        send_email_use_case.email_handler, "send_email", new_callable=AsyncMock
    )
    mock_send_email.return_value = (False, "Mailgun")

    result = await send_email_use_case.execute(mock_email_create)

    assert result.status == Status.FAILED.value
    assert result.provider == "Mailgun"
    assert result.sent_at is None
    mock_create_email.assert_called_once_with(mock_email_create)
    mock_send_email.assert_called_once_with(mock_email)
    mock_update_email_status.assert_called_once_with(result)
