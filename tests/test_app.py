from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_from_zero.app import app

client = TestClient(app)


def test_read_root_must_return_ok():
    """Test read_root must return ok."""
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def test_read_root_must_return_messge():
    """Test read_root must return message."""
    client = TestClient(app)
    response = client.get('/')
    assert response.json() == {
        'message': 'Basic FastAPI design for standard project'
    }
