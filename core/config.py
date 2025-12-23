import os

class Settings:
    APP_NAME = "Vet Clinic API"
    ENV = os.getenv("ENV", "dev")

settings = Settings()
