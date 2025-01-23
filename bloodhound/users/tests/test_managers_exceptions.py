from unittest import TestCase

from bloodhound.users.managers import UserManager
from bloodhound.users.models import User


class TestUserManagerExceptions(TestCase):
    def test_create_user_email_is_none(self):
        self.user_manager = UserManager()

        with self.assertRaises(ValueError) as context:
            self.user_manager._create_user(email=None, password="@strong!%pass12-=")
        self.assertEqual(str(context.exception), "The email address must be set")

    def test_create_superuser_is_staff_false_raises_valueerror(self):
        self.user_manager = User.objects
        # Test that a ValueError is raised when is_staff=False
        with self.assertRaises(ValueError) as context:
            self.user_manager.create_superuser(
                email="admin@example1.com",
                password="password123",
                is_staff=False,  # This should cause an error
            )
            self.assertEqual(
                str(context.exception), "Superuser must have is_staff=True"
            )

    def test_create_superuser_is_superuser_false_raises_valueerror(self):
        self.user_manager = User.objects
        with self.assertRaises(ValueError) as context:
            self.user_manager.create_superuser(
                email="admin@example2.com",
                password="password123",
                is_superuser=False,  # This should cause an error.
            )
        self.assertEqual(
            str(context.exception), "superuser must have is_superuser=True."
        )
