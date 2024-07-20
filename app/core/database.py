from typing import Any, Generator

from sqlmodel import Session, SQLModel, create_engine

from app.core.settings import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)


def get_db() -> Generator[Session, Any, None]:
    with Session(engine) as session:
        yield session


def init_db() -> None:
    SQLModel.metadata.create_all(engine)
