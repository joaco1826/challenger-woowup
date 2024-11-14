from datetime import datetime

import pytest
from mongoengine import connect, disconnect
from mongomock import MongoClient
from app.adapters.database.email_repository import EmailRepository
from app.constants.database import Status
from app.core.entities.email import EmailCreate, Email
from app.models.email_model import EmailModel


@pytest.fixture
def mock_db():
    connect(
        "mongoenginetest",
        host="mongodb://localhost",
        mongo_client_class=MongoClient,
        uuidRepresentation="standard"
    )
    yield
    disconnect()


@pytest.fixture
def repository():
    return EmailRepository()


@pytest.mark.asyncio
async def test_save_email(mock_db, repository):
    record = EmailCreate(
        recipient="users@gmail.com",
        sender="jforeroola@gmail.com",
        body="test email",
        subject="test email"
    )
    saved_record = await repository.create_email(record)

    assert saved_record.email_uuid is not None
    assert saved_record.recipient == "users@gmail.com"


@pytest.mark.asyncio
async def test_get_email_by_id(mock_db, repository):
    record = EmailCreate(
        recipient="users@gmail.com",
        sender="jforeroola@gmail.com",
        body="test email",
        subject="test email"
    )
    saved_record = await repository.create_email(record)
    retrieved_record = await repository.get_email_by_id(saved_record.email_uuid)

    assert retrieved_record.recipient == saved_record.recipient
    assert retrieved_record.sender == saved_record.sender


@pytest.mark.asyncio
async def test_update_email_status_success(mock_db, repository):
    email_doc = EmailModel(
        email_uuid="1234",
        recipient="users@gmail.com",
        sender="jforeroola@gmail.com",
        subject="Test Email",
        body="This is a test email.",
        status=Status.PENDING.value,
        provider=None,
        created_at=datetime.utcnow(),
    )
    email_doc.save()

    email_data = Email(
        email_uuid="1234",
        recipient="users@gmail.com",
        sender="jforeroola@gmail.com",
        subject="Test Email",
        body="This is a test email.",
        status=Status.SENT.value,
        provider="SendGrid",
        sent_at=datetime.utcnow(),
        created_at=email_doc.created_at,
    )

    updated_doc = await repository.update_email_status(email_data)

    assert updated_doc is not None
    assert updated_doc.status == Status.SENT.value
    assert updated_doc.provider == "SendGrid"

    db_doc = EmailModel.objects(email_uuid="1234").first()
    assert db_doc.status == Status.SENT.value
    assert db_doc.provider == "SendGrid"


@pytest.mark.asyncio
async def test_update_email_status_not_found(mock_db, repository):
    email_data = Email(
        email_uuid="9999",
        recipient="users@gmail.com",
        sender="jforeroola@gmail.com",
        subject="Test Email",
        body="This is a test email.",
        status=Status.SENT.value,
        provider="SendGrid",
        sent_at=datetime.utcnow(),
        created_at=datetime.utcnow(),
    )

    updated_doc = await repository.update_email_status(email_data)

    assert updated_doc is None
