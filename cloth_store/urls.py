from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import admin_dashboard  # Import custom admin view

urlpatterns = [
    # 1. Django's built-in Admin (Moved to a secret path)
    path('backend-admin/', admin.site.urls),

    # 2. Your Custom Admin Dashboard
    path('admin/', admin_dashboard, name='admin_dashboard'),

    # 3. Accounts App (Login, Register, Dashboard, Password Reset)
    path('', include('accounts.urls')),

    # 4. Store App (Shop, Cart, Orders, Admin Actions)
    path('store/', include('store.urls')),
]

# Serve media files (Images) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)