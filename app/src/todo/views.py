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
        todos = Todo.query.all()
        return jsonify({'todos': todos_schema.dump(todos)}), 200

    @jwt_required
    def post(self):
        title = request.json.get('title')
        errors = todo_schema.validate({'title': title})
        if errors:
            return jsonify({'msg': errors}), 400
        user_id = get_jwt_identity()
        todo = Todo(title=title)
        todo.user_id = user_id
        todo.save()
        return jsonify({'msg': 'Todo has been created'}), 200


class TodoChangeView(views.MethodView):
    method = ('GET', 'POST')

    @jwt_required
    def put(self, todo_id):
        title, completed = request.json.get('title'), request.json.get('completed')
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.title = title
        todo.completed = completed
        todo.save()
        return jsonify({'todo': todo_schema.dump(todo)}), 200

    @jwt_required
    def delete(self, todo_id):
        Todo.query.filter_by(id=todo_id).first().delete()
        return jsonify({'msg': 'Todo has been deleted'}), 200

    @jwt_required
    def get(self, todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        return jsonify(todo_schema.dump(todo)), 200


blueprint.add_url_rule(f'{URL_RESOURCE}', view_func=TodoView.as_view('todos'))
blueprint.add_url_rule(f'{URL_RESOURCE}/<todo_id>', view_func=TodoChangeView.as_view('change_todos'))
