import pytest

@pytest.mark.auth
@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected_status, expected_message",
    [
        ("user", "wrong-password",401,"Invalid credentials"),
        ("nonexistent-user", "demo",401,"Invalid credentials"),
    ]
)
def test_invalid_login(
    base_url,
    api_session,
    username,
    password,
    expected_status,
    expected_message
):
    # Arrange
    url = f"{base_url}/learning/auth/login"

    payload = {
        "username": username,
        "password": password,
    }

    # Act
    response = api_session.post(url,json=payload)
    data = response.json()

    # Assert
    assert response.status_code== expected_status
    assert data["error"]["message"] == expected_message


@pytest.mark.auth
@pytest.mark.regression
@pytest.mark.parametrize(
    "payload, expected_status, expected_message",
    [
        pytest.param(
            {"username": "", "password": "demo"},
            401,
            "Invalid credentials",
            id="empty_username"
        ),
        pytest.param(
            {"username": "user", "password": ""},
            401,
            "Invalid credentials",
            id="empty_password"
        ),
        pytest.param(
            {"password": "demo"},
            401,
            "Invalid credentials",
            id="missing_username"
        ),
        pytest.param(
            {"username": "user"},
            401,
            "Invalid credentials",
            id="missing_password"
        ),
        pytest.param(
            {},
            401,
            "Invalid credentials",
            id="missing_all_fields"
        ),
    ]
)
def test_login_with_missing_or_empty_fields(
    base_url,
    api_session,
    payload,
    expected_status,
    expected_message
):
    # Arrange
    url = f"{base_url}/learning/auth/login"

    # Act
    response = api_session.post(url,json=payload)
    data = response.json()

    # Assert
    assert response.status_code== expected_status
    assert data["error"]["message"] == expected_message



@pytest.mark.smoke
@pytest.mark.auth
@pytest.mark.regression
def test_login_success(base_url, api_session):
    # Arrange
    url = f"{base_url}/learning/auth/login"

    payload = {
        "username": "user",
        "password": "demo",
    }

    # Act
    response = api_session.post(url,json=payload)
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert data["success"] is True
    assert "access_token" in data
    assert "id" in data
    assert data["username"] == "user"