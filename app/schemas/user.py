from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator, ConfigDict

from app.enums import Gender


class UserCreate(BaseModel):
    username: str = Field(min_length=1, max_length=16, description="用户名", examples=["admin"])
    password: str = Field(min_length=6, max_length=64, description="密码", examples=["123456"])
    name: str | None = Field(default=None, max_length=32, description="姓名", examples=["Bob"])
    gender: Gender | None = Field(default=None, description="性别", examples=["M"])
    age: int | None = Field(default=None, gt=0, le=150, description="年龄", examples=[18])
    height: Decimal | None = Field(default=None, ge=0, le=300, description="身高", examples=[168.86])
    weight: float | None = Field(default=None, gt=0, lt=200, description="体重", examples=[60.11])
    birthday: date | None = Field(default=None, description="生日", examples=[date(2001, 8, 1)])
    status: bool | None = Field(default=None, description="状态", examples=[True])
    create_time: datetime | None = Field(
        default=None,
        description="创建时间",
        alias="createTime",
        examples=[datetime.now()]
    )

    @field_validator("birthday")
    @classmethod
    def validate_birthday_not_future(cls, birthday: date | None) -> date | None:
        if birthday is not None:
            today = datetime.now().date()
            if birthday > today:
                raise ValueError(f"生日不能晚于今天（{today}）")
        return birthday


class UserCreateResponse(BaseModel):
    user_id: int = Field(description="用户ID", examples=[1001])


class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int = Field(description="用户ID", examples=[1001])
    username: str = Field(description="用户名", examples=["bob"])
    name: str | None = Field(default=None, description="姓名", examples=["Bob"])
    gender: Gender | None = Field(default=None, description="性别", examples=["M"])
    age: int | None = Field(default=None, description="年龄", examples=[18])
    height: Decimal | None = Field(default=None, description="身高", examples=[168.86])
    weight: float | None = Field(default=None, description="体重", examples=[60.11])
    birthday: date | None = Field(
        default=None,
        description="生日",
        examples=[date(2001, 8, 1), "2011-05-06"]
    )
    status: bool | None = Field(default=None, description="状态", examples=[True])
    create_time: datetime | None = Field(
        default=None,
        description="创建时间",
        alias="createTime",
        examples=[datetime.now()]
    )
