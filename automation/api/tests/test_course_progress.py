import json
from pathlib import Path

import pytest


DATA_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "course_progress_auth.json"
)


with open(DATA_FILE, encoding="utf-8") as file:
    AUTH_CASES = json.load(file)

@pytest.mark.auth
@pytest.mark.regression
@pytest.mark.parametrize(
    "case",
    AUTH_CASES,
    ids=[case["id"] for case in AUTH_CASES]
)
def test_course_progress_with_invalid_auth(
    base_url,
    api_session,
    case
):
    # Arrange
    url = f"{base_url}/learning/courses/1/progress"

    headers = {}

    if case["authorization"] is not None:
        headers["Authorization"] = case["authorization"]

    # Act
    response = api_session.get(url, headers=headers)
    data = response.json()

    # Assert
    assert response.status_code == case["expected_status"]
    assert data["error"]["message"] == case["expected_message"]

@pytest.mark.auth
@pytest.mark.regression
def test_course_progress_with_valid_auth(
    base_url,
    enrolled_course
):
    # Arrange
    session = enrolled_course["session"]
    course_id = enrolled_course["course_id"]

    url = f"{base_url}/learning/courses/{course_id}/progress"

    # Act
    response = session.get(url)
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert "progress" in data
    assert isinstance(data["progress"], (int, float))