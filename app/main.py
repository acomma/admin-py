from fastapi import FastAPI

from app.routers import user

app = FastAPI(title="后台管理系统")

app.include_router(user.router)
