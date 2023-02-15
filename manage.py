from flask.cli import FlaskGroup

from app import create_app, db

app = create_app()

cli = FlaskGroup(app)


# Create a terminal command to initialize db and create all tables from scratch
# Called as " python manage.py create_db "
@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()