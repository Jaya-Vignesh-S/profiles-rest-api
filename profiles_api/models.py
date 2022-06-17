from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for uSER pROFILES"""

    def create_user(self,email,name,password=None):
        """Cfreate a new user Profile"""
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user with given details"""
        user = self.create_user(email=email,name=name,password=password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email =models.EmailField(max_lenght=225, unique=True)
    name = models.charfield(max_lenght=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Retrive Full name of user"""
        return self.name

    def get_short_names(self):
        """Retrive short name for User"""
        return self.name

    def __str__(self):
        """return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    # ForeignKeys links models to other models in Django
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE  # If the user profile is removed, the profile feed item will be deleted.
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text



# Create your models here.
