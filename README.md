# MarsClothStore 🛍️

A premium, luxury-themed e-commerce platform for online clothing retail built with Django and modern glassmorphism design.

---

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Database Setup](#database-setup)
- [Usage Guide](#usage-guide)
- [Admin Panel](#admin-panel)
- [API Routes](#api-routes)

---

## ✨ Features

### User Features
- **User Authentication**
  - Sign up and account registration
  - Secure login with email/password
  - Password recovery with OTP verification
  - Profile management

- **Shopping Experience**
  - Browse products by category (Men, Women, Accessories)
  - Product filtering and search
  - Add items to shopping cart
  - View order history

- **Checkout & Payments**
  - Shopping cart management
  - Secure payment gateway integration
  - Order confirmation with reference number
  - Payment status tracking

### Admin Features
- **Product Management**
  - Add, edit, and delete products
  - Upload product images
  - Manage inventory and pricing
  - Organize products by category

- **Order Management**
  - View all customer orders
  - Update order status (Pending → Paid → Dispatched → Delivered)
  - Track payment submissions
  - Monitor order details

- **User Management**
  - View all registered users
  - Manage user information
  - Track user activity
  - Admin profile settings

### Design Features
- **Luxury Dark Theme**
  - Glassmorphism UI with backdrop blur effects
  - Premium luxury fabric background texture
  - Gold accent color (#d4af37)
  - Smooth animations and transitions
  - Responsive design for all devices

---

## 📁 Project Structure

```
cloth_store/
├── manage.py                          # Django management script
├── README.md                          # This file
├── .env                               # Environment variables
│
├── cloth_store/                       # Main Django project settings
│   ├── settings.py                    # Project configuration
│   ├── urls.py                        # Main URL routing
│   ├── asgi.py                        # ASGI configuration
│   └── wsgi.py                        # WSGI configuration
│
├── accounts/                          # Authentication app
│   ├── models.py                      # User models
│   ├── views.py                       # Auth views (login, register, password reset)
│   ├── urls.py                        # Auth routes
│   ├── utils.py                       # Helper functions (OTP, email)
│   ├── forms.py                       # Authentication forms
│   └── migrations/                    # Database migrations
│
├── store/                             # E-commerce app
│   ├── models.py                      # Product, Cart, Order models
│   ├── views.py                       # Store, cart, admin views
│   ├── urls.py                        # Store routes
│   ├── forms.py                       # Product and profile forms
│   ├── admin.py                       # Django admin configuration
│   └── migrations/                    # Database migrations
│
├── templates/                         # HTML templates
│   ├── login.html                     # Login page
│   ├── register.html                  # Registration page
│   ├── dashboard.html                 # User dashboard
│   ├── shop.html                      # Product listing
│   ├── cart.html                      # Shopping cart
│   ├── my_orders.html                 # Order history
│   ├── orders.html                    # Public orders view
│   ├── payment.html                   # Payment page
│   ├── payment_done.html              # Payment confirmation
│   ├── order_success.html             # Order confirmation
│   ├── forgot_password.html           # Password recovery
│   ├── reset_password.html            # Password reset
│   ├── verify_otp.html                # Email verification
│   ├── verify_reset_otp.html          # Reset password verification
│   └── custom_admin/                  # Admin panel templates
│       ├── dashboard.html             # Admin products
│       ├── users.html                 # User management
│       ├── orders.html                # Order management
│       └── product_form.html          # Add/edit products & profile
│
├── static/                            # Static files
│   ├── css/
│   │   └── style.css                  # Global styles
│   └── js/
│       └── auth.js                    # Authentication scripts
│
└── media/                             # User uploads
    └── products/                      # Product images
```

---

## 🛠 Tech Stack

- **Backend:** Django 4.x
- **Database:** SQLite (default) or PostgreSQL
- **Frontend:** HTML5, CSS3, JavaScript
- **Authentication:** Django Auth with OTP verification
- **Payment:** Integration ready for payment gateway
- **Styling:** CSS Glassmorphism with modern design patterns

---

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Steps

1. **Clone or Navigate to Project**
   ```bash
   cd /Users/mars/Desktop/Store/cloth_store
   ```

2. **Create Virtual Environment** (if not already created)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or install manually:
   ```bash
   pip install django
   pip install pillow  # For image handling
   ```

---

## ⚙️ Configuration

### Environment Variables (.env)
Create a `.env` file in the root directory based on `.env.example`:

```env
# Django Configuration
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_ENGINE=django.db.backends.mysql
DB_NAME=cloth_store_db
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

**Important:** Never commit the `.env` file to version control. Use `.env.example` as a template. See [SECURITY.md](SECURITY.md) for detailed security guidelines.

### Settings (cloth_store/settings.py)
- Database configured for MySQL (configurable via environment variables)
- Static files configuration for CSS and JavaScript
- Media files for product images
- Email backend for OTP and password recovery

---

## 🚀 Running the Application

### 1. Make Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### 3. Start Development Server
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

---

## 🗄️ Database Setup

### Initial Models
- **User** (Django's built-in User model)
- **Product** (Name, Price, Category, Description, Image)
- **Cart** (User cart items with quantities)
- **Order** (Order details with status tracking)
- **OrderItem** (Individual items in orders)

### Migrations
All migrations are pre-configured. Simply run:
```bash
python manage.py migrate
```

---

## 👥 Usage Guide

### For Customers

1. **Register/Login**
   - Visit `/accounts/register/` to create account
   - Or login at `/accounts/login/`
   - Email verification via OTP

2. **Browse Products**
   - Navigate to `/store/` or `/` (Shop)
   - Filter by category: Men, Women, Accessories
   - Click on products to view details

3. **Shopping Cart**
   - Click "Add to Cart" on products
   - View cart at `/store/cart/`
   - Adjust quantities or remove items

4. **Checkout**
   - Proceed to payment page
   - Complete payment
   - Receive order confirmation

5. **View Orders**
   - Check order history at `/store/my-orders/`
   - Track order status and payment

### For Admins

1. **Access Admin Panel**
   - Login with admin account
   - Navigate to `/store/admin/`

2. **Manage Products**
   - View all products at dashboard
   - Add new product: `/store/admin/add-product/`
   - Edit product: Click edit link in table
   - Delete products from the list

3. **Manage Orders**
   - View all orders: `/store/admin/orders/`
   - Update order status (Pending → Paid → Dispatched → Delivered)
   - Track payment information

4. **Manage Users**
   - View registered users: `/store/admin/users/`
   - Monitor user activity
   - Delete inactive users

5. **Profile Settings**
   - Update admin profile: `/store/admin/profile/`
   - Change name and email

---

## 🔗 API Routes

### Authentication Routes (`/accounts/`)
| Route | Method | Purpose |
|-------|--------|---------|
| `/login/` | GET, POST | User login |
| `/register/` | GET, POST | User registration |
| `/logout/` | GET | User logout |
| `/forgot-password/` | GET, POST | Password recovery initiation |
| `/verify-otp/` | GET, POST | Email OTP verification |
| `/reset-password/<uuid>/` | GET, POST | Password reset |
| `/verify-reset-otp/` | GET, POST | Reset password OTP verification |

### Store Routes (`/store/`)
| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Shop homepage |
| `/?category=<name>` | GET | Category filter |
| `/cart/` | GET, POST | View/manage shopping cart |
| `/add-to-cart/<id>/` | POST | Add product to cart |
| `/remove-from-cart/<id>/` | GET | Remove from cart |
| `/orders/` | GET | Orders list (public) |
| `/my-orders/` | GET | User order history |
| `/payment/` | GET, POST | Payment page |
| `/payment-done/` | GET | Payment confirmation |
| `/order-success/` | GET | Order confirmation |

### Admin Routes (`/store/admin/`)
| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Product inventory |
| `/add-product/` | GET, POST | Add new product |
| `/edit-product/<id>/` | GET, POST | Edit product |
| `/delete-product/<id>/` | POST | Delete product |
| `/users/` | GET | User management |
| `/delete-user/<id>/` | POST | Delete user |
| `/orders/` | GET, POST | Order management |
| `/profile/` | GET, POST | Admin profile |

---

## 🎨 Design & Theme

### Color Palette
- **Primary:** #050505 (Deep Black)
- **Accent:** #d4af37 (Luxury Gold)
- **Text:** #ffffff (White)
- **Muted:** #888888 (Grey)

### Typography
- **Headings:** Playfair Display (Serif, Italic)
- **Body:** Poppins (Sans-serif, Modern)

### Effects
- **Glassmorphism** with 20px blur
- **Backdrop filters** for depth
- **Smooth transitions** (0.3-0.4s)
- **Gold accents** on hover
- **Luxury fabric background** (parallax)

---

## 📝 Notes

- All templates use consistent luxury dark theme
- Product images uploaded to `/media/products/`
- Static files (CSS, JS) in `/static/` directory
- Email verification requires SMTP configuration
- Payment gateway integration ready for implementation

---

## 🔒 Security

- CSRF protection on all forms
- Login required decorators on protected views
- Admin-only access to management features
- Password hashing with Django's default system
- OTP-based password recovery
- Environment variables for sensitive data (SECRET_KEY, database credentials, email passwords)
- See [SECURITY.md](SECURITY.md) for complete security guidelines and best practices
- OTP-based password recovery

---

## 📞 Support

For issues or questions about the project structure, refer to:
- Django Documentation: https://docs.djangoproject.com/
- Project Views: `store/views.py` and `accounts/views.py`
- Templates: All HTML in `/templates/` directory

---

**MarsClothStore** - Premium Online Fashion Retail Platform ✨
