from sqlalchemy import Column, DateTime, text
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    email: str
    password: str


class UserRegist(UserBase):
    user_name: str
    verify_code: str


class User(SQLModel, table=True):
    __tablename__ = "user"
    id: int = Field(
        sa_column=Column(INTEGER, primary_key=True, autoincrement=True, comment="编号"),
    )
    email: str = Field(sa_column=Column(VARCHAR(20), nullable=False, comment="邮箱"))
    user_name: str = Field(
        sa_column=Column(VARCHAR(20), nullable=False, comment="用户名")
    )
    password: str = Field(
        sa_column=Column(VARCHAR(100), nullable=False, comment="密码")
    )
    login_time: int = Field(sa_column=Column(INTEGER, comment="登录时间"))
    create_date: int = Field(
        sa_column=Column(
            DateTime, comment="创建时间", server_default=text("CURRENT_TIMESTAMP")
        )
    )
    update_date: int = Field(
        sa_column=Column(
            DateTime,
            comment="更新时间",
            server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        )
    )
