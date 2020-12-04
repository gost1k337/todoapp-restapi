from flask import jsonify
from src.todo.models import Todo
from src.todo.schemas import todo_schema, todos_schema
from src.database import db


class TodoService(object):
    def create_todo(self, user_id, title):
        todo = Todo(title=title)
        todo.user_id = user_id
        todo.save()
        return todo, 200

    def get_todo(self, todo_id):
        if not self.is_todo_exists(todo_id):
            return jsonify({'msg': 'Todo does not exists'}), 404
        todo = Todo.query.filter_by(id=todo_id).first()
        return jsonify(todo_schema.dump(todo)), 200

    def get_todos(self):
        todos = Todo.query.all()
        return jsonify({'todos': todos_schema.dump(todos)}), 200

    def change_todo(self, todo_id, title, completed):
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.title = title
        todo.completed = completed
        todo.save()
        return jsonify(todo_schema.dump(todo)), 200

    def delete_todo(self, todo_id):
        Todo.query.filter_by(id=todo_id).first().delete()
        return jsonify({'msg': 'Todo has been deleted'}), 200

    def is_todo_exists(self, todo_id):
        return db.session.query(db.exists().where(Todo.id == todo_id)).scalar()

