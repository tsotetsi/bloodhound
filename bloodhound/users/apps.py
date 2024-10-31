import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bloodhound.users"

    def ready(self) -> None:
        with contextlib.suppress(ImportError):
            import bloodhound.users.signals  # noqa F401
