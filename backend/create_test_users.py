
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
    print("👤 [SCRIPT] Gestionando usuarios de prueba...")
    
    # 1. Admin User
    admin_email = 'admin@example.com'
    admin_pass = 'securepassword123'
    
    try:
        user = User.objects.get(email=admin_email)
        user.set_password(admin_pass)
        user.save()
        print(f"🔄 [UPDATE] Usuario Admin actualizado: {admin_email} / {admin_pass}")
    except User.DoesNotExist:
        User.objects.create_superuser(
            email=admin_email,
            password=admin_pass
        )
        print(f"✅ [CREATE] Usuario Admin creado: {admin_email} / {admin_pass}")

    # 2. External User (Standard)
    user_email = 'usuario@prueba.com'
    user_pass = 'prueba12345'
    
    try:
        user = User.objects.get(email=user_email)
        user.set_password(user_pass)
        user.save()
        print(f"🔄 [UPDATE] Usuario Externo actualizado: {user_email} / {user_pass}")
    except User.DoesNotExist:
        User.objects.create_user(
            email=user_email,
            password=user_pass,
            rol=User.Rol.EXTERNO
        )
        print(f"✅ [CREATE] Usuario Externo creado: {user_email} / {user_pass}")

if __name__ == '__main__':
    create_users()
