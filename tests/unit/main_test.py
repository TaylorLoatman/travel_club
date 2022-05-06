from main import app


def test_home():
    app.testing = True
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Travel Club' in response.data

