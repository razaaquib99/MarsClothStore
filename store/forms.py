from django import forms
from .models import Product
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Product Name'}),
            'price': forms.NumberInput(attrs={'class': 'glass-input', 'placeholder': 'Price'}),
            'category': forms.Select(attrs={'class': 'glass-input'}),
            'description': forms.Textarea(attrs={'class': 'glass-input', 'placeholder': 'Description', 'rows': 4}),
            'image': forms.FileInput(attrs={'class': 'glass-input'}),
        }

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'glass-input', 'placeholder': 'Email Address'}),
        }