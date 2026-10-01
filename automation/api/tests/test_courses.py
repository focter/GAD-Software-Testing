import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_get_courses(base_url, api_session):
    # Arrange
    url = f"{base_url}/learning/courses"


    # Act
    response = api_session.get(url)
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(data,list)
    assert len(data)>0

@pytest.mark.smoke
@pytest.mark.regression
def test_get_course_detail(base_url, api_session):
    # Arrange
    url = f"{base_url}/learning/courses/1"

    # Act
    response = api_session.get(url)
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(data,dict)
    assert data["id"]==1
    assert "title" in data

@pytest.mark.regression
@pytest.mark.parametrize(
    "course_id, expected_status, expected_message",
    [
        (99999, 404, "Course not found"),
        (0, 404, "Course not found"),
        (-1, 404, "Course not found"),
        ("abc", 404, "Course not found"),
    ]
)
def test_get_invalid_course(
    base_url,
    api_session,
    course_id,
    expected_status,
    expected_message
):
    # Arrange
    url = f"{base_url}/learning/courses/{course_id}"

    # Act
    response = api_session.get(url)
    data = response.json()

    # Assert
    assert response.status_code== expected_status
    assert data["error"]["message"] == expected_message