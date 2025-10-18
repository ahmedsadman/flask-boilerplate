from app.models import User


def test_create_user(client, db_session):
    payload = {"id": 1, "name": "test user", "email": "test@email.com"}
    response = client.post("/user/", json=payload)
    assert response.status_code == 200

    data = response.get_json()
    assert data == payload

    db_obj = db_session.query(User).filter_by(email=payload["email"]).first()
    assert db_obj is not None
