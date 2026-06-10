import pytest
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status


def test_api_root_lists_main_endpoints(api_client):
    response = api_client.get(reverse("api-root"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == "Django Secure Auth API"
    assert response.data["endpoints"]["swagger"].endswith("/api/docs/")
    assert response.data["endpoints"]["health"].endswith("/api/v1/health/")
    assert response.data["endpoints"]["password_reset"].endswith(
        "/api/v1/auth/password-reset/"
    )


def test_openapi_schema_is_public(api_client):
    response = api_client.get(reverse("schema"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data["info"]["title"] == "Django Secure Auth API"
    assert "/api/v1/auth/login/" in response.data["paths"]


def test_swagger_ui_is_public(api_client):
    response = api_client.get(reverse("swagger-ui"))

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_health_check_returns_ok(api_client):
    response = api_client.get(reverse("health"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"status": "ok"}


@pytest.mark.django_db
def test_register_creates_user(api_client):
    response = api_client.post(
        reverse("register"),
        {
            "username": "matheus",
            "email": "matheus@example.com",
            "password": "SenhaForte123!",
            "password_confirm": "SenhaForte123!",
        },
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {
        "id": response.data["id"],
        "username": "matheus",
        "email": "matheus@example.com",
    }
    assert "password" not in response.data


@pytest.mark.django_db
def test_register_returns_standard_validation_error(api_client):
    response = api_client.post(
        reverse("register"),
        {
            "username": "matheus",
            "email": "matheus@example.com",
            "password": "SenhaForte123!",
            "password_confirm": "senha-diferente",
        },
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "errors" in response.data
    assert "password_confirm" in response.data["errors"]


@pytest.mark.django_db
def test_login_returns_jwt_tokens(api_client, user):
    response = api_client.post(
        reverse("login"),
        {"email": user.email, "password": "SenhaForte123!"},
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_login_invalid_credentials_returns_generic_message(api_client, user):
    response = api_client.post(
        reverse("login"),
        {"email": user.email, "password": "senha-errada"},
        format="json",
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.data == {"detail": "Credenciais invalidas."}


@pytest.mark.django_db
def test_refresh_token_returns_new_access_token(api_client, user):
    login_response = api_client.post(
        reverse("login"),
        {"email": user.email, "password": "SenhaForte123!"},
        format="json",
    )

    response = api_client.post(
        reverse("token-refresh"),
        {"refresh": login_response.data["refresh"]},
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data


@pytest.mark.django_db
def test_logout_blacklists_refresh_token(api_client, user):
    login_response = api_client.post(
        reverse("login"),
        {"email": user.email, "password": "SenhaForte123!"},
        format="json",
    )
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {login_response.data['access']}")

    response = api_client.post(
        reverse("logout"),
        {"refresh": login_response.data["refresh"]},
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"detail": "Logout realizado com sucesso."}


@pytest.mark.django_db
def test_logout_requires_refresh_token(api_client, user):
    login_response = api_client.post(
        reverse("login"),
        {"email": user.email, "password": "SenhaForte123!"},
        format="json",
    )
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {login_response.data['access']}")

    response = api_client.post(reverse("logout"), {}, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {
        "errors": {
            "refresh": ["This field is required."],
        }
    }


@pytest.mark.django_db
def test_me_requires_authentication(api_client):
    response = api_client.get(reverse("me"))

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_me_returns_authenticated_user(authenticated_api_client, user):
    response = authenticated_api_client.get(reverse("me"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }


@pytest.mark.django_db
def test_change_password_requires_current_password(authenticated_api_client):
    response = authenticated_api_client.post(
        reverse("change-password"),
        {
            "current_password": "senha-errada",
            "new_password": "NovaSenhaForte123!",
            "new_password_confirm": "NovaSenhaForte123!",
        },
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "errors" in response.data


@pytest.mark.django_db
def test_change_password_updates_user_password(authenticated_api_client, user):
    response = authenticated_api_client.post(
        reverse("change-password"),
        {
            "current_password": "SenhaForte123!",
            "new_password": "NovaSenhaForte123!",
            "new_password_confirm": "NovaSenhaForte123!",
        },
        format="json",
    )

    user.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert user.check_password("NovaSenhaForte123!")


@pytest.mark.django_db
def test_password_reset_request_sends_email_for_existing_user(api_client, user):
    response = api_client.post(
        reverse("password-reset"),
        {"email": user.email},
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "detail": (
            "Se o email estiver cadastrado, enviaremos instrucoes "
            "para redefinir a senha."
        )
    }
    assert len(mail.outbox) == 1
    assert user.email in mail.outbox[0].to
    assert "uid:" in mail.outbox[0].body
    assert "token:" in mail.outbox[0].body


@pytest.mark.django_db
def test_password_reset_request_does_not_reveal_missing_email(api_client):
    response = api_client.post(
        reverse("password-reset"),
        {"email": "missing@example.com"},
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "detail": (
            "Se o email estiver cadastrado, enviaremos instrucoes "
            "para redefinir a senha."
        )
    }
    assert len(mail.outbox) == 0


@pytest.mark.django_db
def test_password_reset_confirm_updates_password(api_client, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    response = api_client.post(
        reverse("password-reset-confirm"),
        {
            "uid": uid,
            "token": token,
            "new_password": "NovaSenhaForte123!",
            "new_password_confirm": "NovaSenhaForte123!",
        },
        format="json",
    )

    user.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"detail": "Senha redefinida com sucesso."}
    assert user.check_password("NovaSenhaForte123!")


@pytest.mark.django_db
def test_password_reset_confirm_rejects_invalid_token(api_client, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    response = api_client.post(
        reverse("password-reset-confirm"),
        {
            "uid": uid,
            "token": "token-invalido",
            "new_password": "NovaSenhaForte123!",
            "new_password_confirm": "NovaSenhaForte123!",
        },
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {
        "errors": {
            "token": ["Token de recuperacao invalido."],
        }
    }
