from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings


def create_booking_confirmation_template(
        booking: dict,
        email_to: EmailStr
):
    email = EmailMessage()
    email["subject"] = "Booking confirmation"
    email["From"] = settings.SMTP_USER
    email["To"] = settings.SMTP_USER

    email.set_content(
        f"""
        <h1>Booking confirmation</h1>
        Your booking is in date ....
        
        """,
        subtype="html"
    )
    return email
