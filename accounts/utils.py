import random
import string
from django.core.mail import send_mail
from django.conf import settings


def generate_otp(length=6):
    """Generate a random OTP of specified length."""
    return ''.join(random.choices(string.digits, k=length))


def send_otp(email, otp):
    """Send OTP to the specified email address."""
    subject = "Your OTP for Email Verification"
    message = f"Your OTP is: {otp}\n\nPlease do not share this OTP with anyone."
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
