from uuid import uuid4

from mongoengine import Document, StringField, DateTimeField
from datetime import datetime


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
    sender = StringField(required=True)
    subject = StringField(required=True)
    body = StringField(required=True)
    provider = StringField(required=False, default="")
    status = StringField(choices=["sent", "failed", "pending"], default="pending")
    created_at = DateTimeField(default=datetime.utcnow)
    sent_at = DateTimeField()
