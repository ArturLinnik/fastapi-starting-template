from pydantic import BaseSettings


class Settings(BaseSettings):

    # Default user
    SUPERUSER_USERNAME: str = "admin"
    SUPERUSER_EMAIL: str = "admin@email.com"
    SUPERUSER_PASSWORD: str = "admin"

    # Database
    POSTGRES_USER: str = "artur"
    POSTGRES_PASSWORD: str = "pokemon"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "test_db3"


settings = Settings()
