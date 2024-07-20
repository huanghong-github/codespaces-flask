from typing import Any, Generator

from sqlmodel import Session, SQLModel, create_engine

from app.core.settings import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)

# 初始化数据库连接:


def get_db() -> Generator[Session, Any, None]:
    with Session(engine) as session:
        yield session


def init_db() -> None:
    SQLModel.metadata.create_all(engine)
