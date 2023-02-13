import os

from flask_migrate import Migrate
from flask_script import Manager

from main import create_app, db

app = create_app()
app.app_context().push()

migrate = Migrate(app, db, command='migrate')
