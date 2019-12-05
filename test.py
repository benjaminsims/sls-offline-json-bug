import requests


def test_big_json():
    endpoint = "http://localhost:3000/bigjson"
    response = requests.get(endpoint)
    assert response.text
    json = response.json()
    return json
