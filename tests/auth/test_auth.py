from flask_login import current_user


def test_invalid_login(client):
    with client:
        response = client.post(
            "/login",
            data={"email": "wrong@example.com", "password": "WrongPassword123"},
            follow_redirects=True,
        )
        assert response.status_code == 200
        assert b"Invalid email or password" in response.data


def test_login(client):
    with client:
        client.post(
            "/login",
            data={"email": "admin@gmail.com", "password": "admin12345"}
        )

        assert current_user.is_authenticated


def test_successful_register(client):
    assert client.get('/register').status_code == 200
    response = client.post('/register', data={'username': "mesi", "email": "messi555@mail.com",
                                              "password": "mesi555", "confirm_password": "messi555"}, follow_redirects=True)

    assert response.request.path == '/register'