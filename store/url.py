from django.urls import path
from . import views

urlpatterns = [
    # Page for "Enter Full Shop"
    path('shop/', views.shop_view, name='shop'),
    
    # Page for "Men", "Women", "Accessories"
    path('shop/<str:category_name>/', views.shop_view, name='shop_category'),
]