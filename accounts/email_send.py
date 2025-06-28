from django.core.mail import EmailMessage
import secrets
import string

def send_email_confirmation(email, token):
    subject = "Confirm your email address"
    message = f"""
    Assalomu alaykum,

    Iltimos, quyidagi havolaga bosib emailingizni tasdiqlang:

    http://localhost:8000/verify-email/?token={token}

    Rahmat.
    """
    email = EmailMessage(subject, message, to=[email])
    email.send()

def generate_temp_password(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

def send_email_confirmation_with_password(email, token):
    temp_password = generate_temp_password()
    subject = "Confirm your email address and temporary password"
    message = f"""
    Assalomu alaykum,

    Sizning vaqtinchalik parolingiz: {temp_password}

    Emailingizni tasdiqlash uchun quyidagi havolaga bosing:
    http://localhost:8000/verify-email/?token={token}

    Rahmat.
    """
    email = EmailMessage(subject, message, to=[email])
    email.send()
    return temp_password