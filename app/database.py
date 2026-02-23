from sqlmodel import create_engine, Session

from app.config import settings

# engine = create_engine(
#     "mysql+mysqlconnector://root:123456@localhost:3306/example?charset=utf8mb4",
#     echo=True
# )

engine = create_engine(
    url=str(settings.sqlalchemy_database_uri),
    echo=True
)


def get_session():
    with Session(engine) as session:
        yield session
