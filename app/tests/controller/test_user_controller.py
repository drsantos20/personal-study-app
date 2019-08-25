from main import app

def test_index_returns_200():
    request, response = app.test_client.get('/')
    assert response.status == 200
    assert (response.json) == {"hello": "world"}


def test_index_put_not_allowed():
    request, response = app.test_client.put('/')
    assert response.status == 405