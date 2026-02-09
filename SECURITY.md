# Security Guidelines

## Environment Variables

This application uses environment variables to protect sensitive information. **Never commit sensitive credentials to the repository.**

### Required Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# Django Configuration
SECRET_KEY=your-secret-key-here-generate-a-new-one
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_ENGINE=django.db.backends.mysql
DB_NAME=cloth_store_db
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password-here
```

### Generating a Secret Key

You can generate a new Django secret key using:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use an online generator: https://djecrety.ir/

### Email Configuration

For Gmail, you'll need to:
1. Enable 2-Factor Authentication on your Google account
2. Generate an App Password: https://myaccount.google.com/apppasswords
3. Use the generated app password in the `EMAIL_HOST_PASSWORD` variable

### Best Practices

1. **Never commit `.env` files** - The `.gitignore` file is configured to exclude `.env` files
2. **Use `.env.example`** - Reference the `.env.example` file to see required variables without exposing actual values
3. **Production Settings** - In production:
   - Set `DEBUG=False`
   - Use strong, unique `SECRET_KEY`
   - Configure `ALLOWED_HOSTS` properly
   - Use environment-specific database credentials
   - Consider using a secrets management service (AWS Secrets Manager, Azure Key Vault, etc.)

### Security Features

This application implements:
- CSRF protection on all forms
- Login required decorators on protected views
- Admin-only access to management features
- Password hashing with Django's default system
- OTP-based password recovery
- Environment variable configuration for sensitive data

### Reporting Security Issues

If you discover a security vulnerability, please email the repository owner directly rather than opening a public issue.
