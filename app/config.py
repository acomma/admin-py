from pydantic import MySQLDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USERNAME: str = "root"
    MYSQL_PASSWORD: str = ""
    MYSQL_DATABASE: str = "test"

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> MySQLDsn:
        return MySQLDsn.build(
            scheme="mysql+mysqlconnector",
            host=self.MYSQL_HOST,
            port=self.MYSQL_PORT,
            username=self.MYSQL_USERNAME,
            password=self.MYSQL_PASSWORD,
            path=self.MYSQL_DATABASE,
            query="charset=utf8mb4"
        )


settings = Settings()
