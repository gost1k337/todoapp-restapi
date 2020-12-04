from flask.cli import FlaskGroup
from src.main import app, db, migrate

cli = FlaskGroup(app)


@cli.command('migrate')
def migrate():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
