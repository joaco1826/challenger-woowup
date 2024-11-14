import httpx
from fastapi import HTTPException
from app.constants.config import Config


class CaptchaValidator:
    @staticmethod
    async def verify_captcha(token: str) -> bool:
        """
        Verifica el token de Google reCAPTCHA.
        :param token: El token generado en el cliente.
        :return: True si es válido, False en caso contrario.
        """
        url = "https://www.google.com/recaptcha/api/siteverify"
        secret_key = Config.RECAPTCHA_SECRET_KEY
        payload = {"secret": secret_key, "response": token}

        async with httpx.AsyncClient() as client:
            response = await client.post(url, data=payload)
            result = response.json()

        if not result.get("success"):
            raise HTTPException(status_code=400, detail="Captcha validation failed.")

        return True
