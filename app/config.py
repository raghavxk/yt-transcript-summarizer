from pydantic import BaseSettings


class EnvSettings(BaseSettings):
    youtube_v3_api_key: str

    class Config:
        env_file = ".env"


settings = EnvSettings()
