from unittest import TestCase

from bloodhound.users.managers import UserManager


class TestUserManagerExceptions(TestCase):
    def setUp(self):
        # Initialize UserManager
        self.user_manager = UserManager()

    def test_create_user_email_is_none(self):
        with self.assertRaises(ValueError) as context:
            self.user_manager._create_user(email=None, password="@strong!%pass12-=")
        self.assertEqual(str(context.exception), "The email address must be set")

    def test_create_superuser_must_be_staff(self):
        pass
