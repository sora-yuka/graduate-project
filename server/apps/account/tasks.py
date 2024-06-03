from django.core.mail import send_mail
from config.celery import app
from decouple import config
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@app.task
def send_verification_code(email: str, verify_code: str) -> None:
    full_link = f"{config('SERVER_IP')}/{verify_code}/"
    html_message = render_to_string("email.html", {"full_link": full_link})
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject="Account verification",
        # message=f"Follow the link to activate your account: {full_link}",
        message=plain_message,
        from_email=config("EMAIL_HOST"),
        recipient_list=[email],
        html_message=html_message
    )
    
@app.task
def send_recovery_code(email: str, verify_code: str, secret: str) -> None:
    full_link = f"{config('SERVER_IP')}/api/v1/user/recover/{verify_code}/"
    
    send_mail(
        subject="Account reset",
        message=f"Follow the link to reset your account credentials: {full_link}"
        + f"\nHere is your secret: {secret}\nDo not share with anyone.",
        from_email=config("EMAIL_HOST"),
        recipient_list=[email]
    )