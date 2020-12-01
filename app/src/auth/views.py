from flask import Blueprint, jsonify, request
from src.services.auth import AuthService
from .models import User
from .schemas import users_schema, user_schema, user_in_schema

auth = AuthService()

URL_RESOURCE = '/api/auth'

blueprint = Blueprint('auth', __name__)


@blueprint.route(f'{URL_RESOURCE}/login', methods=('POST',))
def login_user():
    email, password = request.json.get('email'), request.json.get('password')
    errors = user_in_schema.validate({'email': email, 'password': password})
    if errors:
        return jsonify({'message': errors}), 400
    return auth.login(email, password)


@blueprint.route(f'{URL_RESOURCE}/register', methods=('POST',))
def register_user():
    username, email, password = request.json.get('username'), request.json.get('email'), \
                                request.json.get('password')
    errors = user_in_schema.validate({'email': email,
                                      'password': password,
                                      'username': username})
    if errors:
        return jsonify({'message': errors}), 400

    return auth.register(email, password, username)


@blueprint.route(f'{URL_RESOURCE}/users', methods=('GET',))
def get_users():
    users = User.query.all()
    return {'users': users_schema.dump(users)}
