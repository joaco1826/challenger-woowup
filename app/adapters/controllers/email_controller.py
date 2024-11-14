from fastapi import APIRouter, HTTPException
from app.core.use_cases.send_email import SendEmail
from app.core.entities.email import EmailBase

router = APIRouter()


@router.post("/emails", tags=["Emails"])
async def send_email(email_data: EmailBase):
    """
    Sends an email and saves its status in the database.

    Args:
        email_data (EmailBase): Email data to send.

    Returns:
        dict: Information about the delivery status.
    """
    send_email_case = SendEmail()

    result = await send_email_case.execute(email_data)

    if result.status == "failed":
        raise HTTPException(status_code=500, detail="No se pudo enviar el correo.")

    return {
        "message": "Correo procesado exitosamente.",
        "status": result.status,
        "sent_at": result.sent_at,
        "created_at": result.created_at,
    }
