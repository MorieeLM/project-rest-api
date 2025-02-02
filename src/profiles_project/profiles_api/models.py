from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles. Helps Django work with our custom user model. """

    def create_user(self, email, name, password=None):
        """Create a new user profile."""
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create a new superuser."""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represent a user profile inside our system """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    """" Object manager to help manage user profiles """

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """" Used to get User's full name """

        return self.name
    
    def get_short_name(self):
        """" Used to get user's short name """

        return self.name
    
    def __str__(self):
        """" Used to convert the object to a string """
        return self.email
    
    

class ProfileFeedItem(models.Model):
    """ Profile Status update """

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)

    created_on = models.DateField(auto_now=True)

    def __str__(self):
        """ return model as a string"""

        return self.status_text