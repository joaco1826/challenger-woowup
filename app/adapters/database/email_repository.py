from app.constants.database import Status
from app.models.email_model import EmailModel
from app.core.entities.email import Email, EmailCreate


class EmailRepository:
    async def create_email(self, email_data: EmailCreate) -> Email:
        email_doc = EmailModel(
            recipient=email_data.recipient,
            subject=email_data.subject,
            body=email_data.body
        )
        email_doc.save()
        return self._to_entity(email_doc)

    async def update_email_status(self, email: Email) -> EmailModel | None:
        email_doc = EmailModel.objects(email_uuid=email.email_uuid).first()
        if email_doc:
            email_doc.status = email.status
            email_doc.provider = email.provider
            if email.status == Status.SENT.value:
                email_doc.sent_at = email.sent_at
            return email_doc.save()

    async def get_email_by_id(self, email_uuid: str) -> Email | None:
        email_doc = EmailModel.objects(email_uuid=email_uuid).first()
        return self._to_entity(email_doc) if email_doc else None

    @staticmethod
    def _to_entity(email_doc: EmailModel) -> Email:
        return Email(
            email_uuid=email_doc.email_uuid,
            recipient=email_doc.recipient,
            sender=email_doc.sender,
            subject=email_doc.subject,
            body=email_doc.body,
            provider=email_doc.provider,
            status=email_doc.status,
            created_at=email_doc.created_at,
            sent_at=email_doc.sent_at,
        )
