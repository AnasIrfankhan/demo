from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=80)
    roll=models.IntegerField()


class role (models.Model):
    name=models.CharField(max_length=100)

    # def __str__(self) :
    #     return self.name


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        if password is None:
            raise ValueError("Password must not be none")
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    username = None
    first_name = models.CharField(max_length=100, null=False)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    # otp = models.CharField(max_length=50)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    # Define the role relationship
    role = models.ManyToManyField(role, blank=True, related_name="CustomUser")


class Employer(models.Model):
    name=models.CharField(max_length=50)
    skills=models.CharField(max_length=50)
    age=models.IntegerField()


class Manager(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()


    # def __str__(self):
    #     return self.name
