from abc import ABC, abstractmethod
from app.core.entities.email import Email


class EmailProvider(ABC):
    @abstractmethod
    async def send_email(self, email: Email) -> (bool, str):
        pass
