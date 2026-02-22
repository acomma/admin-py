from sqlmodel import create_engine, Session

engine = create_engine(
    "mysql+mysqlconnector://root:123456@localhost:3306/example?charset=utf8mb4",
    echo=True
)


def get_session():
    with Session(engine) as session:
        yield session
