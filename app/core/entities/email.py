from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

from app.constants.database import Status


class EmailCreate(BaseModel):
    sender: EmailStr
    recipient: EmailStr = "jforeroola@gmail.com"
    subject: str
    body: str


class Email(EmailCreate):
    email_uuid: str
    provider: str
    status: Status
    created_at: datetime
    sent_at: datetime
    
    
class ResponseBase(BaseModel):
    success: bool
    message: str
    data: Optional[Email] = None
