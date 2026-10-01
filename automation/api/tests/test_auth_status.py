import pytest


@pytest.mark.smoke
@pytest.mark.auth
def test_auth_status_without_auth(base_url, api_session):
    url = f"{base_url}/learning/auth/status"

    response = api_session.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data["authenticated"] is False

@pytest.mark.auth
def test_auth_status_with_valid_auth(
    base_url,
    authenticated_session
):
    # Arrange
    session, login_data = authenticated_session
    url = f"{base_url}/learning/auth/status"

    # Act
    response = session.get(url)
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert data["authenticated"] is True
    assert data["user"]["id"] == login_data["id"]