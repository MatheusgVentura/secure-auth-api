import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()


@pytest.mark.django_db
def test_create_user_with_email_login():
    user = User.objects.create_user(
        username="matheus",
        email="matheus@example.com",
        password="SenhaForte123!",
    )

    assert user.email == "matheus@example.com"
    assert user.check_password("SenhaForte123!")
    assert user.is_staff is False
    assert str(user) == "matheus@example.com"


@pytest.mark.django_db
def test_create_superuser_sets_required_flags():
    user = User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="SenhaForte123!",
    )

    assert user.is_staff is True
    assert user.is_superuser is True


@pytest.mark.django_db
def test_email_must_be_unique():
    User.objects.create_user(
        username="matheus",
        email="matheus@example.com",
        password="SenhaForte123!",
    )

    with pytest.raises(IntegrityError):
        User.objects.create_user(
            username="other",
            email="matheus@example.com",
            password="SenhaForte123!",
        )
