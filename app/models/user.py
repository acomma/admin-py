from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Column, VARCHAR, TypeDecorator
from sqlmodel import SQLModel, Field

from app.enums import Gender


class GenderTypeDecorator(TypeDecorator):
    impl = VARCHAR(1)
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return value.value

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return Gender(value)


class User(SQLModel, table=True):
    __tablename__ = "t_user"

    id: int | None = Field(default=None, primary_key=True, description="用户ID")
    username: str = Field(description="用户名")
    password: str = Field(description="密码")
    name: str | None = Field(description="姓名")
    # gender: Gender | None = Field(sa_column=Column(VARCHAR(1)), description="性别")
    gender: Gender | None = Field(sa_column=Column(GenderTypeDecorator()), description="性别")
    age: int | None = Field(description="年龄")
    height: Decimal | None = Field(description="身高")
    weight: float | None = Field(description="体重")
    birthday: date | None = Field(description="生日")
    status: bool | None = Field(description="状态")
    create_time: datetime | None = Field(description="创建时间")
