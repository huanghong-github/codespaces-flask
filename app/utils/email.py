import emails

from app.core import settings


class Email:
    def __init__(self):
        smtp_options = {"host": settings.SMTP_HOST, "port": settings.SMTP_PORT}
        if settings.SMTP_TLS:
            smtp_options["tls"] = True
        elif settings.SMTP_SSL:
            smtp_options["ssl"] = True
        if settings.SMTP_USER:
            smtp_options["user"] = settings.SMTP_USER
        if settings.SMTP_PASSWORD:
            smtp_options["password"] = settings.SMTP_PASSWORD
        self.smtp_options = smtp_options

    @classmethod
    def send(
        cls,
        *,
        email_to: str,
        subject: str = "",
        html_content: str = "",
    ) -> None:
        message = emails.Message(
            subject=subject,
            html=html_content,
            mail_from=(settings.EMAILS_FROM_NAME, settings.EMAILS_FROM_EMAIL),
        )

        response = message.send(to=email_to, smtp=cls.smtp_options)
        return response
