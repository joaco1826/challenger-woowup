from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class EmailBase(BaseModel):
    sender: EmailStr
    recipient: EmailStr = "jforeroola@gmail.com"
    subject: str
    body: str


class Email(EmailBase):
    email_uuid: Optional[str] = None
    provider: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    sent_at: Optional[datetime] = None
