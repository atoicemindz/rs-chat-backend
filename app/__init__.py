from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from .config import DATABASE_URL
from .routes import main_bp

def create_app():
    load_dotenv()  # Load .env file

    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
