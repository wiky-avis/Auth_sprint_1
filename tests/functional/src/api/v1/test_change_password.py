from http import HTTPStatus

import pytest

from src.repositories.auth_repository import AuthRepository
from tests.functional.vars.auth import TEST_PUBLIC_KEY, sign_jwt
from tests.functional.vars.tables import CLEAN_TABLES


@pytest.mark.usefixtures("clean_table")
@pytest.mark.parametrize("clean_table", [CLEAN_TABLES], indirect=True)
def test_change_password(test_db, test_client, setup_url, monkeypatch):
    email = "test66@test.ru"
    old_password = "abraabra"
    new_password = "abracadabra"
    auth_repository = AuthRepository(test_db)
    auth_repository.create_user(email=email)
    user = auth_repository.get_user_by_email(email=email)
    auth_repository.set_password(user, old_password)
    monkeypatch.setattr("src.config.Config.JWT_PUBLIC_KEY", TEST_PUBLIC_KEY)
    headers = {"X-Auth-Token": sign_jwt(str(user.id))}

    res = test_client.patch(
        "/api/v1/users/change_password",
        json={"old_password": old_password, "new_password": new_password},
        headers=headers,
    )
    assert res.status_code == HTTPStatus.OK
    body = res.json
    assert body == {"success": True, "error": None, "result": "Ok"}


def test_change_password_error_404(test_client, setup_url, monkeypatch):
    user_id = "bbbbbbbb-9be4-4066-be89-695d35ea9131"
    old_password = "abraabra"
    new_password = "abracadabra"
    monkeypatch.setattr("src.config.Config.JWT_PUBLIC_KEY", TEST_PUBLIC_KEY)
    headers = {"X-Auth-Token": sign_jwt(str(user_id))}

    res = test_client.patch(
        "/api/v1/users/change_password",
        json={"old_password": old_password, "new_password": new_password},
        headers=headers,
    )
    assert res.status_code == HTTPStatus.NOT_FOUND
    body = res.json
    assert body == {
        "success": False,
        "error": {"msg": "User does not exist"},
        "result": None,
    }


@pytest.mark.usefixtures("clean_table")
@pytest.mark.parametrize("clean_table", [CLEAN_TABLES], indirect=True)
def test_change_password_error_400(
    test_db, test_client, setup_url, monkeypatch
):
    email = "test11@test.ru"
    new_password = "abracadabra"
    auth_repository = AuthRepository(test_db)
    auth_repository.create_user(email=email)
    user = auth_repository.get_user_by_email(email=email)
    monkeypatch.setattr("src.config.Config.JWT_PUBLIC_KEY", TEST_PUBLIC_KEY)
    headers = {"X-Auth-Token": sign_jwt(str(user.id))}

    res = test_client.patch(
        "/api/v1/users/change_password",
        json={"old_password": "", "new_password": new_password},
        headers=headers,
    )
    assert res.status_code == HTTPStatus.BAD_REQUEST
    body = res.json
    assert body == {
        "success": False,
        "error": {"msg": "No new password or no old password."},
        "result": None,
    }


@pytest.mark.usefixtures("clean_table")
@pytest.mark.parametrize("clean_table", [CLEAN_TABLES], indirect=True)
def test_change_password_error_401(
    test_db, test_client, setup_url, monkeypatch
):
    email = "test10@test.ru"
    bad_password = "12mkhyd"
    old_password = "abraabra"
    new_password = "abracadabra"
    auth_repository = AuthRepository(test_db)
    auth_repository.create_user(email=email)
    user = auth_repository.get_user_by_email(email=email)
    auth_repository.set_password(user, bad_password)
    monkeypatch.setattr("src.config.Config.JWT_PUBLIC_KEY", TEST_PUBLIC_KEY)
    headers = {"X-Auth-Token": sign_jwt(str(user.id))}

    res = test_client.patch(
        "/api/v1/users/change_password",
        json={"old_password": old_password, "new_password": new_password},
        headers=headers,
    )
    assert res.status_code == HTTPStatus.UNAUTHORIZED
    body = res.json
    assert body == {
        "success": False,
        "error": {"msg": "Invalid password."},
        "result": None,
    }
