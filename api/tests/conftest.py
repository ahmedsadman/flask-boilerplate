import pytest
from app import create_app, db
from config import Config


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


@pytest.fixture()
def app():
    app = create_app(TestConfig)

    with app.app_context():
        from app.models import User  # noqa: F401

        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture()
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture()
def db_session(app):
    with app.app_context():
        yield db.session
