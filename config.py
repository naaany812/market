import os

# - Текущая папка
current_path = os.path.dirname(os.path.realpath(__file__))
# - Путь к файлу БД в данной папке
db_path = "sqlite:///" + current_path + "\\test.db"


class Config:
    DEBUG = True
    SECRET_KEY = 'It is my shop! My shop is cool'
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
