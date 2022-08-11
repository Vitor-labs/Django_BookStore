from django.core.mail import EmailMessage
from django.conf import settings

class Utils:
    @staticmethod
    def send_email(data):
        email_body = data['email_body']
        email_subject = data['email_subject']
        email_to = data['email_to']
        email_from = settings.EMAIL_HOST_USER

        email = EmailMessage(
            subject=email_subject, 
            body=email_body,
            from_email=email_from,
            to=[email_to]
            )

        email.send()