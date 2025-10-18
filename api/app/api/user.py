from app.repo import UserRepo


class UserAPI:
    @staticmethod
    def create_user(name: str, email: str, commit_now: bool = True):
        u = UserRepo.create(name=name, email=email)
        return u
