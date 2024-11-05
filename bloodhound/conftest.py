import pytest

from bloodhound.users.models import User
from bloodhound.users.tests.factories import UserFactory


@pytest.fixture
def user(db) -> User:
    return UserFactory()
