from app.models import User
from app import db
from app.utils import commit_or_rollback


class UserRepo:
    @staticmethod
    def create(name: str, email: str, commit_now: bool = True):
        u = User(name=name, email=email)
        db.session.add(u)

        if commit_now:
            commit_or_rollback(db.session)

        return u
