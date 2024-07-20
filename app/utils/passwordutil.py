import re

from passlib.context import CryptContext


class PasswordUtil:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        return cls.pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def password_hash(cls, password):
        return cls.pwd_context.hash(password)

    @classmethod
    def password_check(cls, password):
        return (
            6 < len(password) < 20
            and re.search(r"[A-Z]+", password)
            and re.search(r"[a-z]+", password)
            and re.search(r"[0-9]+", password)
        )
