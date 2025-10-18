from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from config import Config

load_dotenv()

cors = CORS()
db = SQLAlchemy()


def create_app(config: type[Config]) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    # dependency
    cors.init_app(app)
    db.init_app(app)

    # blueprints
    from app.routes import main_bp
    from app.routes import user_bp

    app.register_blueprint(main_bp, url_prefix="/")
    app.register_blueprint(user_bp, url_prefix="/user")

    from app.errors import APIError

    @app.errorhandler(Exception)
    def handle_api_error(error: Exception):
        print(error)
        if isinstance(error, APIError):
            response = error.to_dict(), error.status_code
        else:
            response = APIError().to_dict(), 500

        return response

    # init db
    with app.app_context():
        from app.models import User  # noqa: F401

        db.create_all()

    # cli commands
    @app.cli.command("reset-db")
    def reset_db():
        db.drop_all()
        db.create_all()

    return app
