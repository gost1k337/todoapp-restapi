from flask import Blueprint, jsonify, request

URL_RESOURCE = '/api/auth'

blueprint = Blueprint('auth', __name__)


@blueprint.route(f'{URL_RESOURCE}/login', methods=('POST',))
def login_user():
    return jsonify({'username': 'name'})

