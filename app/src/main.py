from flask import Flask
from .extensions import db, migrate
from . import config
from . import auth


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app)


def register_blueprints(app):
    app.register_blueprint(auth.views.blueprint)


app = create_app()


@app.route('/')
def home():
    return 'hello world'
