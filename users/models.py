import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from . import choices


class UserManager(BaseUserManager):

    @staticmethod
    def _validate_user(email: str, phone_number: str):
        if not email:
            raise ValueError('Users must have an email address')

        if not phone_number:
            raise ValueError('Users must have an phone number')

    def create_user(self, email: str, phone_number: str, password: str = None) -> 'User':
        """
        Creates and saves a User with the given email and phone number.
        """
        self._validate_user(email=email, phone_number=phone_number)

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            is_active=True,
        )
        user.set_unusable_password()
        user.save()

        return user

    def create_superuser(self, email: str, phone_number: str, password: str = None) -> 'User':
        """
        Creates and saves a superuser with the given email, phone number and password.
        """
        self._validate_user(email=email, phone_number=phone_number)

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        user.set_password(password)
        user.save()

        return user


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True)
    user_type = models.CharField(
        max_length=10,
        choices=choices.UserTypeChoices.choices,
        blank=True,
        null=True,
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()
