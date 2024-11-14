from fastapi import APIRouter, HTTPException
from app.core.use_cases.send_email import SendEmail
from app.core.entities.email import EmailCreate, ResponseBase

router = APIRouter()


@router.post("/emails", tags=["Emails"], responses={
    400: {
        "description": "Bad request",
        "content": {
            "application/json": {
                "example": {"detail": "The email could not be sent."}
            }
        }
    }
})
async def send_email(email_data: EmailCreate) -> ResponseBase | HTTPException:
    """
    Sends an email and saves its status in the database.

    Args:
        email_data (EmailCreate): Email data to send.

    Returns:
        dict: Information about the delivery status.
    """
    send_email_case = SendEmail()

    result = await send_email_case.execute(email_data)

    if result.status == "failed":
        raise HTTPException(status_code=400, detail="The email could not be sent.")

    return ResponseBase(
        success=True,
        message="Email processed successfully.",
        data=result
    )
