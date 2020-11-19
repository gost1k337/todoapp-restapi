from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from . import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
# migrate = Migrate()


@app.route('/')
def home():
    return 'hello world'