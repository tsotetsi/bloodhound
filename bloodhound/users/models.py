from typing import ClassVar

from django.db import models
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for Bloodhound Application.
    """

    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type ignore[assignment]
    last_name = None  # type ignore[assignment]
    email = EmailField(_("email address"), unique=True)
    username = None  # type ignore[assignment]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """
        Get URL for user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"pk": self.id})
