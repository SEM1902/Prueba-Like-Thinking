from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """Manager personalizado para el modelo User"""
    
    def create_user(self, email, password=None, **extra_fields):
        """Crea y guarda un usuario con el email y password dados"""
        if not email:
            raise ValueError('El usuario debe tener un email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """Crea y guarda un superusuario"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('rol', User.Rol.ADMINISTRADOR)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Modelo de usuario personalizado"""
    
    class Rol(models.TextChoices):
        ADMINISTRADOR = 'ADMINISTRADOR', 'Administrador'
        EXTERNO = 'EXTERNO', 'Externo'
    
    email = models.EmailField(unique=True, verbose_name='Correo electrónico')
    rol = models.CharField(max_length=20, choices=Rol.choices, default=Rol.EXTERNO, verbose_name='Rol')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return self.email
