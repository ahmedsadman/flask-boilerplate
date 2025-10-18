from flask import Blueprint, request
from app.api import UserAPI

user_bp = Blueprint("user", __name__)


@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    user = UserAPI.create_user(data["name"], data["email"])
    return user.to_dict()
