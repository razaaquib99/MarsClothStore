from django.db import models
from django.contrib.auth.models import User

# --- 1. Product Model ---
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Accessories', 'Accessories'),
    ]
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# --- 2. Cart Model ---
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

# --- 3. Order Model ---
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Payment_Submitted', 'Payment Submitted'),
        ('Paid', 'Paid'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    utr_number = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

# --- 4. Order Item Model (To store history) ---
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"