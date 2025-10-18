from flask import Blueprint
from sqlalchemy import text
from app import db
from app.errors import DBConnectionError

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return {"message": "OK"}


@main_bp.route("/ping")
def ping():
    try:
        db.session.execute(text("SELECT 1"))
        return "pong"
    except Exception:
        raise DBConnectionError()
