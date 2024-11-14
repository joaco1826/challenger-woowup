from fastapi import APIRouter, HTTPException

from app.constants.database import Status
from app.constants.email import EmailConstants
from app.core.use_cases.send_email import SendEmail
from app.core.entities.email import ResponseBase, EmailCaptcha
from app.utils.captcha import CaptchaValidator

router = APIRouter()


@router.post("/emails", tags=["Emails"], responses={
    400: {
        "description": "Bad request",
        "content": {
            "application/json": {
                "example": {"detail": EmailConstants.MESSAGE_EMAIL_FAILED}
            }
        }
    }
})
async def send_email(
        email_data: EmailCaptcha
) -> ResponseBase or HTTPException:
    """
    Sends an email and saves its status in the database.

    Args:
        email_data (EmailCaptcha): Email data to send.

    Returns:
        dict: Information about the delivery status.
    """
    await CaptchaValidator.verify_captcha(email_data.captcha_token)

    send_email_case = SendEmail()

    result = await send_email_case.execute(email_data)

    if result.status == Status.FAILED.value:
        raise HTTPException(status_code=400, detail=EmailConstants.MESSAGE_EMAIL_FAILED)

    return ResponseBase(
        success=True,
        message=EmailConstants.MESSAGE_EMAIL_SUCCESS,
        data=result
    )
