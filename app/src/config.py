import os

SQLALCHEMY_DATABASE_URI = f'postgresql://' \
                          f'{os.environ["POSTGRES_USER"]}:' \
                          f'{os.environ["POSTGRES_PW"]}@' \
                          f'{os.environ["POSTGRES_HOST"]}/' \
                          f'{os.environ["POSTGRES_DB"]}' \
