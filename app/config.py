from decouple import config

class Settings:
    DATABASE_URL = config("DATABASE_URL", default="sqlite:///./ecommerce.db")
    SECRET_KEY = config("SECRET_KEY", default="your_secret_key")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()
