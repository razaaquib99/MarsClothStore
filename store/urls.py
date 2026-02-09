from django.urls import path
from . import views

urlpatterns = [
    # --- Public Shop ---
    path('shop/', views.shop_view, name='shop'),
    path('shop/<str:category_name>/', views.shop_view, name='shop_category'),
    
    # --- Cart & Checkout ---
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    path('checkout/', views.checkout, name='checkout'),
    path('payment/<int:order_id>/', views.payment_view, name='payment_view'),
    path('my-orders/', views.my_orders, name='my_orders'),

    # --- Custom Admin Panel Actions ---
    # (Note: The main /admin/ path is handled in the project-level urls.py)
    
    # Product Management
    path('admin/add/', views.add_product, name='add_product'),
    path('admin/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('admin/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    
    # User Management
    path('admin/users/', views.admin_users, name='admin_users'),
    path('admin/users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    
    # Order Management
    path('admin/orders/', views.admin_orders, name='admin_orders'),
    path('admin/orders/update/<int:order_id>/', views.update_order_status, name='update_order_status'),
    
    # Admin Profile
    path('admin/profile/', views.edit_admin_profile, name='edit_admin_profile'),
]