from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager,)

# Custom user manager to manage our users
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
# Admin user manager
class AdminUserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)

#Get all users with the role is_birth_centre_administrator    
class EndUserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_enduser=True)

# custom user model to handle users   
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    is_superuser = None
    is_staff = None
    is_enduser = models.BooleanField(null=True, default=False)
    is_admin = models.BooleanField(null=True, default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        
    ]
    
    objects = CustomUserManager()
    endUser = EndUserManager()
    adminUser = AdminUserManager()

# End user model    
class EndUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

#Admin user model
class AdminUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
