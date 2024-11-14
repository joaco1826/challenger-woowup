from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

from app.constants.database import Status
from app.constants.email import Recipients


class EmailCreate(BaseModel):
    sender: EmailStr
    recipient: Recipients
    subject: str
    body: str


class Email(EmailCreate):
    email_uuid: str
    provider: str
    status: Status
    created_at: datetime
    sent_at: Optional[datetime] = None


class ResponseBase(BaseModel):
    success: bool
    message: str
    data: Optional[Email] = None
