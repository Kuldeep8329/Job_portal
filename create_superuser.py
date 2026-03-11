"""
Run with: python create_superuser.py
Creates a default admin user for the Django admin panel.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal_project.settings')
django.setup()

from django.contrib.auth.models import User

ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'admin@jobmatch.ai'
ADMIN_PASSWORD = 'Admin@1234'

if not User.objects.filter(username=ADMIN_USERNAME).exists():
    User.objects.create_superuser(ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD)
    print(f"✅ Superuser created!")
    print(f"   Username: {ADMIN_USERNAME}")
    print(f"   Password: {ADMIN_PASSWORD}")
    print(f"   Admin URL: http://127.0.0.1:8000/admin/")
else:
    print(f"ℹ️  Superuser '{ADMIN_USERNAME}' already exists.")
    print(f"   Admin URL: http://127.0.0.1:8000/admin/")
