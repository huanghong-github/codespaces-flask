from sqlmodel import select

from app.models.user import User


class UserService:
    def __init__(self, session) -> None:
        self.session = session

    def get_user_by_email(self, email):
        sql = select(User).where(User.email == email)
        return self.session.exec(sql).first()

    def get_user_by_id(self, user_id):
        sql = select(User).where(User.id == user_id)
        return self.session.exec(sql).first()

    def save(self, user):
        self.session.add(user)
        self.session.commit()
