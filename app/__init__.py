from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()

def create_app(config_class = Config):
    #Initialize Flask application and configure from Config class
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints and associated routes
    from app.main import bp
    app.register_blueprint(bp)

    # Initialize database 
    db.init_app(app)

    return app