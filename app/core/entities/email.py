from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

from app.constants.database import Status
from app.constants.email import Senders


class EmailCreate(BaseModel):
    recipient: EmailStr
    subject: str
    body: str


class EmailCaptcha(EmailCreate):
    captcha_token: str


class Email(EmailCreate):
    sender: Optional[Senders] = None
    email_uuid: str
    provider: str
    status: Status
    created_at: datetime
    sent_at: Optional[datetime] = None


class ResponseBase(BaseModel):
    success: bool
    message: str
    data: Optional[Email] = None
