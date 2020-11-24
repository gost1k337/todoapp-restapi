from flask import Flask
from .extensions import db, migrate, ma, jwt
from . import config
from . import auth


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)


def register_blueprints(app: Flask):
    app.register_blueprint(auth.views.blueprint)


app = create_app()
