from typing import Annotated

from fastapi import APIRouter, Path, HTTPException, status

from app.dependencies import SessionDepend
from app.models.user import User
from app.schemas.user import UserCreate, UserCreateResponse, UserPublic

router = APIRouter(prefix="/users", tags=["用户"])


# @router.post("/", summary="创建用户")
# async def create_user(c: UserCreate) -> int:
#     return random.randint(1, 10000)


# @router.post("/", summary="创建用户", responses={
#     200: {
#         "content": {"application/json": {"schema": {"title": "Integer"}}}
#     }
# })
# async def create_user(c: UserCreate) -> int:
#     return random.randint(1, 10000)


@router.post("/", summary="创建用户")
async def create_user(c: UserCreate, session: SessionDepend) -> UserCreateResponse:
    u = User.model_validate(c)
    session.add(u)
    session.commit()
    session.refresh(u)
    return UserCreateResponse(user_id=u.id)


# @router.get("/{user_id}", summary="获取用户")
# async def read_user(
#         user_id: Annotated[int, Path(description="用户ID", example=1001)],
#         session: SessionDepend
# ) -> UserPublic | None:
#     u = session.get(User, user_id)
#     if u is None:
#         return None
#     p = UserPublic.model_validate(u)
#     return p


@router.get("/{userId}", summary="获取用户")
async def read_user(
        user_id: Annotated[
            int,
            Path(
                description="用户ID",
                alias="userId",
                examples=[1001],
                json_schema_extra={
                    "example": 1001
                }
            )
        ],
        session: SessionDepend
) -> UserPublic:
    u = session.get(User, user_id)
    if u is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    p = UserPublic.model_validate(u)
    return p
