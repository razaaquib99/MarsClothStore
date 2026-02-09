from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Product, Cart, Order, OrderItem
from .forms import ProductForm 

# --- Public Views ---

def shop_view(request, category_name=None):
    if category_name:
        products = Product.objects.filter(category=category_name)
        title = f"{category_name} Collection"
    else:
        products = Product.objects.all()
        title = "All Collections"
    
    return render(request, 'shop.html', {'products': products, 'page_title': title})

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        return redirect('shop')
        
    total_price = sum(item.total_price for item in cart_items)
    
    # Create Order
    order = Order.objects.create(
        user=request.user,
        total_amount=total_price,
        status='Pending'
    )
    
    # Move items to OrderItem and Clear Cart
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
        item.delete()
        
    return redirect('payment_view', order_id=order.id)

@login_required
def payment_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if request.method == 'POST':
        utr = request.POST.get('utr')
        order.utr_number = utr
        order.status = 'Payment_Submitted'
        order.save()
        return render(request, 'payment_done.html')
        
    return render(request, 'payment.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_orders.html', {'orders': orders})


# --- Admin Views ---

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_dashboard(request):
    # This view lists products for the admin
    products = Product.objects.all()
    return render(request, 'custom_admin/dashboard.html', {'products': products})

@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm()
    return render(request, 'custom_admin/product_form.html', {'form': form, 'title': 'Add Product', 'button_text': 'Add Product'})

@user_passes_test(is_admin)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'custom_admin/product_form.html', {'form': form, 'title': 'Edit Product', 'button_text': 'Update Product'})

@user_passes_test(is_admin)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('admin_dashboard')

@user_passes_test(is_admin)
def admin_users(request):
    from django.contrib.auth.models import User
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'custom_admin/users.html', {'users': users})

@user_passes_test(is_admin)
def delete_user(request, user_id):
    from django.contrib.auth.models import User
    user = get_object_or_404(User, id=user_id)
    if not user.is_superuser:
        user.delete()
    return redirect('admin_users')

@user_passes_test(is_admin)
def admin_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'custom_admin/orders.html', {'orders': orders})

@user_passes_test(is_admin)
def update_order_status(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
    return redirect('admin_orders')

@user_passes_test(is_admin)
def edit_admin_profile(request):
    from .forms import AdminProfileForm
    
    if request.method == 'POST':
        form = AdminProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = AdminProfileForm(instance=request.user)
    
    return render(request, 'custom_admin/product_form.html', {
        'title': 'Edit Profile',
        'button_text': 'Save Changes',
        'form': form
    })