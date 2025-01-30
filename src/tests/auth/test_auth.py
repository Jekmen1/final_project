from flask_login import current_user


def test_invalid_login(client):
    response = client.post(
        "/login",
        data={"email": "wrong@example.com", "password": "WrongPassword123"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Invalid email or password" in response.data
