from uuid import uuid4

from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

from app.constants.database import Status


class EmailModel(Document):
    meta = {
        'indexes': [
            'email_uuid',
            'recipient',
            'sender',
            'status'
        ],
        'collection': 'emails'
    }

    email_uuid = StringField(
        default=lambda: str(uuid4()),
    )
    recipient = StringField(required=True)
    sender = StringField(required=False, default=None)
    subject = StringField(required=True)
    body = StringField(required=True)
    provider = StringField(required=False, default="")
    status = StringField(choices=Status.values(), default=Status.PENDING.value)
    created_at = DateTimeField(default=datetime.utcnow)
    sent_at = DateTimeField()
