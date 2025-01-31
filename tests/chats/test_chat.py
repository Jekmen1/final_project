from flask_login import current_user

def test_chat_access_unauthenticated(client):
    with client:
        response = client.get("/chat", follow_redirects=True)
        assert response.status_code == 200
        assert b"Login" in response.data
        assert b"Chat Rooms" not in response.data



def test_chat_access_authenticated(client):
    with client:
        client.post(
            "/login",
            data={"email": "admin@gmail.com", "password": "admin12345"}
        )
        response = client.get("/chat", follow_redirects=True)
        assert response.status_code == 200
        assert b"Chat Rooms" in response.data
        assert current_user.is_authenticated


