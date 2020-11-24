from flask import Blueprint, jsonify, request
from src.extensions import db
from flask_jwt_extended import jwt_required, create_access_token
from src.services.auth import AuthService
from .models import User
from .schemas import users_schema, user_schema

auth = AuthService()

URL_RESOURCE = '/api/auth'

blueprint = Blueprint('auth', __name__)


@blueprint.route(f'{URL_RESOURCE}/login', methods=('POST',))
def login_user():
    return auth.login(request)


@blueprint.route(f'{URL_RESOURCE}/register', methods=('POST',))
def register_user():
    return auth.register(request)


@blueprint.route(f'{URL_RESOURCE}/users', methods=('GET',))
def get_users():
    users = User.query.all()
    return {'users': users_schema.dump(users)}
