from flask import Blueprint, jsonify, request, views
from src.services.todo import TodoService
from .schemas import todo_schema, todos_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import Todo


auth = TodoService()

URL_RESOURCE = '/api/todos'

blueprint = Blueprint('todo', __name__)


class TodoView(views.MethodView):
    methods = ('GET', 'POST')

    @jwt_required
    def get(self):
        return auth.get_todos(), 200

    @jwt_required
    def post(self):
        title = request.json.get('title')
        errors = todo_schema.validate({'title': title})
        if errors:
            return jsonify({'msg': errors}), 400
        user_id = get_jwt_identity()
        auth.create_todo(user_id, title)
        return jsonify({'msg': 'Todo has been created'}), 200


class TodoChangeView(views.MethodView):
    method = ('GET', 'POST')

    @jwt_required
    def put(self, todo_id):
        title, completed = request.json.get('title'), request.json.get('completed')
        return auth.change_todo(todo_id, title, completed)

    @jwt_required
    def delete(self, todo_id):
        auth.delete_todo(todo_id)

    @jwt_required
    def get(self, todo_id):
        return auth.get_todo(todo_id)


blueprint.add_url_rule(f'{URL_RESOURCE}', view_func=TodoView.as_view('todos'))
blueprint.add_url_rule(f'{URL_RESOURCE}/<todo_id>', view_func=TodoChangeView.as_view('change_todos'))
