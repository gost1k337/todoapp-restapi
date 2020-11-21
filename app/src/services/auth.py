from src.config import SECRET_KEY
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import jwt
import os

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = 'HS256'


class AuthService(object):
    def login(self):
        pass

    def create_user(self):
        pass
