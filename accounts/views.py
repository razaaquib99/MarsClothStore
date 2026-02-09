from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

from .models import EmailOTP
import random


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp(email, otp):
    subject = "Verify Login Access | MarsClothStore"
    
    # 1. The Professional HTML Design
    html_message = f"""
    <div style="font-family: 'Helvetica Neue', Arial, sans-serif; max-width: 600px; margin: 0 auto; background-color: #f4f4f4; padding: 40px;">
        <div style="background-color: #111; padding: 30px; text-align: center; border-radius: 4px 4px 0 0;">
            <h1 style="color: #d4af37; margin: 0; font-family: 'Georgia', serif; font-style: italic;">MarsClothStore</h1>
        </div>
        
        <div style="background-color: #ffffff; padding: 40px; border-radius: 0 0 4px 4px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
            <p style="color: #555; font-size: 16px; margin-top: 0;">Hello,</p>
            <p style="color: #555; font-size: 16px; line-height: 1.5;">
                We received a request to access your account. To proceed securely, please use the One-Time Password (OTP) below.
            </p>
            
            <div style="text-align: center; margin: 35px 0;">
                <span style="display: inline-block; font-size: 32px; font-weight: bold; letter-spacing: 5px; color: #d4af37; background-color: #000; padding: 15px 30px; border-radius: 4px;">{otp}</span>
            </div>
            
            <p style="color: #999; font-size: 14px; margin-bottom: 0;">
                *For your security, please do not share this code with anyone. If you did not attempt to log in, you can safely ignore this email.
            </p>
        </div>
        
        <div style="text-align: center; margin-top: 20px; color: #888; font-size: 12px;">
            &copy; 2026 MarsClothStore. All rights reserved.<br>
            This is an automated security message.
        </div>
    </div>
    """
    
    # 2. Plain Text Version (Fallback for old devices)
    plain_message = f"MarsClothStore Login Verification\n\nYour OTP Code is: {otp}\n\nPlease do not share this code."
    
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    
    # 3. Send the email with both versions
    send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message)


def register(request):
    if request.method == "POST":
        # 1. Get the name from the form
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            return render(request, "register.html", {"error": "User already exists"})

        # 2. Save the name into the 'first_name' field
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=full_name,  # <--- Saving name here
            is_active=False,
        )

        otp = generate_otp()
        EmailOTP.objects.create(user=user, otp=otp)
        send_otp(email, otp)

        request.session["otp_user"] = user.id
        return redirect("verify_otp")

    return render(request, "register.html")


# accounts/views.py

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)
        if user is None:
            return render(request, "login.html", {"error": "Invalid credentials"})

        # Logic stays: Generate OTP for EVERYONE (including Admins)
        otp = generate_otp()
        EmailOTP.objects.create(user=user, otp=otp)
        send_otp(email, otp)

        request.session["otp_user"] = user.id
        return redirect("verify_otp")

    return render(request, "login.html")



def verify_otp(request):
    user_id = request.session.get("otp_user")
    
    if not user_id:
        return redirect("login")

    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        
        try:
            user = User.objects.get(id=user_id)
            otp_obj = EmailOTP.objects.filter(user=user).last()
        except User.DoesNotExist:
            return redirect("login")

        if otp_obj and otp_obj.otp == entered_otp:
            # 1. Activate and Clean up
            user.is_active = True
            user.save()
            otp_obj.delete()

            # 2. Actually Log them in
            login(request, user)
            
            # --- 👇 SECURE ROUTING LOGIC 👇 ---
            if user.is_superuser:
                # If Admin -> Go to Custom Admin Panel
                return redirect("admin_dashboard") 
            else:
                # If Regular User -> Go to Shop Dashboard
                return redirect("dashboard")       
            # ----------------------------------

        return render(request, "verify_otp.html", {"error": "Invalid OTP"})

    return render(request, "verify_otp.html")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


def logout_view(request):
    logout(request)
    return redirect("login")

# accounts/views.py

# ... existing imports ...

def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        
        # Check if user exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # For security, don't reveal if user doesn't exist, just pretend it worked
            # or show error if you prefer debugging ease
            return render(request, "forgot_password.html", {"error": "User with this email does not exist."})

        # Generate and Send OTP
        otp = generate_otp()
        EmailOTP.objects.create(user=user, otp=otp)
        send_otp(email, otp)

        # Store user ID in session to retrieve it in the next step
        request.session["reset_user_id"] = user.id
        return redirect("verify_reset_otp")

    return render(request, "forgot_password.html")


def verify_reset_otp(request):
    user_id = request.session.get("reset_user_id")
    if not user_id:
        return redirect("forgot_password")

    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        user = User.objects.get(id=user_id)
        
        # Check OTP
        otp_obj = EmailOTP.objects.filter(user=user).last()
        if otp_obj and otp_obj.otp == entered_otp:
            # OTP is valid!
            # Set a flag in session so they can access the change password page
            request.session["can_reset_password"] = True
            
            # Clean up used OTP
            EmailOTP.objects.filter(user=user).delete()
            return redirect("reset_password")
        else:
            return render(request, "verify_reset_otp.html", {"error": "Invalid OTP"})

    return render(request, "verify_reset_otp.html")


def reset_password(request):
    # Security check: User must have passed the OTP step
    if not request.session.get("can_reset_password"):
        return redirect("forgot_password")
    
    user_id = request.session.get("reset_user_id")
    if not user_id:
        return redirect("forgot_password")

    if request.method == "POST":
        new_password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
             return render(request, "reset_password.html", {"error": "Passwords do not match"})

        user = User.objects.get(id=user_id)
        user.set_password(new_password)
        user.save()

        # Clean up session
        del request.session["reset_user_id"]
        del request.session["can_reset_password"]

        return redirect("login")

    return render(request, "reset_password.html")