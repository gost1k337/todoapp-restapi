import os

SQLALCHEMY_DATABASE_URI = f'postgresql://' \
                          f'{os.environ["POSTGRES_USER"]}:' \
                          f'{os.environ["POSTGRES_PW"]}@' \
                          f'{os.environ["POSTGRES_HOST"]}/' \
                          f'{os.environ["POSTGRES_DB"]}' \

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.getenv('SECRET_KEY')
