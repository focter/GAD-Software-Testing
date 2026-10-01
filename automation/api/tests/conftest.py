from pathlib import Path
import sys

from pytest_metadata.plugin import metadata_key
import pytest
import requests


API_ROOT = Path(__file__).resolve().parent.parent

if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))

from config import ENVIRONMENTS

def pytest_html_report_title(report):
    report.title = "GAD API Automation Test Report"


def pytest_configure(config):
    env = config.getoption("--env")

    config.stash[metadata_key]["Project"] = "GAD API Automation"
    config.stash[metadata_key]["Environment"] = env
    config.stash[metadata_key]["Api Base URL"] = ENVIRONMENTS[env]
    
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="local",
        choices=tuple(ENVIRONMENTS),
        help="test environment: local, test, staging"
    )


@pytest.fixture(scope="session")
def base_url(request):
    env = request.config.getoption("--env")
    return ENVIRONMENTS[env]


@pytest.fixture
def api_session():
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture
def authenticated_session(base_url, api_session):
    login_data = {
        "username": "user",
        "password": "demo",
    }

    response = api_session.post(
        f"{base_url}/learning/auth/login",
        json=login_data
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert "access_token" in data
    assert "id" in data

    api_session.headers.update({
        "Authorization": f"Bearer {data['access_token']}"
    })

    return api_session, data

@pytest.fixture
def enrolled_course(base_url, authenticated_session):
    session, login_data = authenticated_session
    course_id = 3

    response = session.post(
        f"{base_url}/learning/courses/{course_id}/enroll",
        json={
            "userId": login_data["id"]
        }
    )

    data = response.json()

    if response.status_code == 200:
        assert data["success"] is True

    elif response.status_code == 400:
        assert data["error"]["message"] == "Already enrolled in this course"

    else:
        pytest.fail(
            f"Unexpected enrollment response: "
            f"{response.status_code}, {data}"
        )

    return {
        "session": session,
        "course_id": course_id,
        "user_id": login_data["id"],
    }