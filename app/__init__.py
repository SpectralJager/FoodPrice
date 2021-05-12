from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from .models import db
from .api_v1_routes import api_v1
from .app_routes import app_router


def create_app():
    app = Flask(__name__)

    # config
    app.secret_key = b'Super_secret_key1337'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # reg extensions
    register_extensions(app)

    # reg blueprints
    app.register_blueprint(api_v1)
    app.register_blueprint(app_router)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app, resources={r'/*': {'origins': '*'}})
