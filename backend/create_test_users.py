
import os
import django
import sys

# Setup Django Environment
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_users():
    # 1. Admin User
    admin_email = 'admin@example.com'
    admin_pass = 'securepassword123'
    if not User.objects.filter(email=admin_email).exists():
        User.objects.create_superuser(
            email=admin_email,
            password=admin_pass
        )
        print(f"✅ Created Admin: {admin_email} / {admin_pass}")
    else:
        print(f"ℹ️ Admin already exists: {admin_email}")

    # 2. External User (Standard)
    user_email = 'usuario@prueba.com'
    user_pass = 'prueba12345'
    if not User.objects.filter(email=user_email).exists():
        User.objects.create_user(
            email=user_email,
            password=user_pass,
            rol=User.Rol.EXTERNO
        )
        print(f"✅ Created User: {user_email} / {user_pass}")
    else:
        print(f"ℹ️ User already exists: {user_email}")

if __name__ == '__main__':
    create_users()
