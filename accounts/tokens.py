from django.utils import timezone
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.conf import settings

signer = TimestampSigner(salt="email-confirmation")

TOKEN_EXPIRY_SECONDS = 3600  # 1 hour for email confirmation

def generate_email_confirmation_token(user):
    temp = signer.sign(user.pk)
    print(f"Generated token: {temp}")
    return temp

def verify_email_confirmation_token(token):
    try:
        unsigned = signer.unsign(token, max_age=TOKEN_EXPIRY_SECONDS)
        return int(unsigned)
    except (BadSignature, SignatureExpired):
        return None