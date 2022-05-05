import requests

API_URL = "http://127.0.0.1:8000"


def test_get_index():
    response = requests.get(
        url=f"{API_URL}/"
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert data["hello"] == "world"


def test_delete_mon_delete():
    response = requests.delete(
        url=f"{API_URL}/mon_delete"
    )
    assert response.status_code == 200, response.content


def test_post_mon_post():
    response = requests.post(
        url=f"{API_URL}/mon_post"
    )
    assert response.status_code == 200, response.content


def test_get_health():
    response = requests.get(
        url=f"{API_URL}/status"
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert data["status"] == 1
