from flask_login import current_user


def test_invalid_login(client):
    with client:
        response = client.post("/login", follow_redirects=True,
                               data={"email": "admin@gmail.com", "password": "wrongpassword"})
        print(response)
