from django.core.mail import send_mail
from config.celery import app
from decouple import config


@app.task
def send_verification_code(email: str, verify_code: str) -> None:
    full_link = f"http://{config('SERVER_IP')}/api/v1/user/verify/{verify_code}/"
    
    send_mail(
        subject="Account verification",
        message=f"Follow the link to activate your account: {full_link}",
        from_email=config("EMAIL_HOST"),
        recipient_list=[email]
    )