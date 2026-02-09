from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # OTP & Dashboard
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Password Reset Flow
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-reset-otp/', views.verify_reset_otp, name='verify_reset_otp'),
    path('reset-password/', views.reset_password, name='reset_password'),
]