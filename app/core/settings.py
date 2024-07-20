from pydantic import computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "AqiMX3NSexKIBLnvo26mFOklTzf9wdh50Vsc48puRYtHC71Pgr"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 24 * 60 * 60

    MYSQL_USER: str = ""
    MYSQL_PASSWORD: str = ""
    MYSQL_HOST: str = ""
    MYSQL_PORT: int = 3306
    MYSQL_DATABASE: str = ""

    SMTP_TLS: bool = True
    SMTP_SSL: bool = False
    SMTP_PORT: int = 587
    SMTP_HOST: str | None = None
    SMTP_USER: str | None = None
    SMTP_PASSWORD: str | None = None

    EMAILS_FROM_EMAIL: str | None = None
    EMAILS_FROM_NAME: str | None = None

    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return str(
            MultiHostUrl.build(
                scheme="mysql+pymysql",
                username=self.MYSQL_USER,
                password=self.MYSQL_PASSWORD,
                host=self.MYSQL_HOST,
                port=self.MYSQL_PORT,
                path=self.MYSQL_DATABASE,
            )
        )

    class Config:
        env_file = ".env"


settings = Settings()
