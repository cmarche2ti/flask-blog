import os


class Config:
    SECRET_KEY = os.getenv("KEY_PHRASE")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("USERNAME")
    MAIL_PASSWORD = os.getenv("PASSWORD")
    ADMIN = os.getenv("ADMIN_EMAIL")
