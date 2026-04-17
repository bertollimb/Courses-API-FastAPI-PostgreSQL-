from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    #General settings used in the application
    API_V1_STR: str = '/api/v1'
    DB_URL: str 

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

settings = Settings()



