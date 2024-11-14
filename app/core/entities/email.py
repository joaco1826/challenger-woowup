from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class EmailCreate(BaseModel):
    sender: EmailStr
    recipient: EmailStr = "jforeroola@gmail.com"
    subject: str
    body: str


class Email(EmailCreate):
    email_uuid: Optional[str] = None
    provider: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    sent_at: Optional[datetime] = None
    
    
class ResponseBase(BaseModel):
    success: bool
    message: str
    data: Optional[Email] = None
