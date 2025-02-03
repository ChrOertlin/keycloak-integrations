from flask import Flask
from flask_cors import CORS
from app.api.routes import register_routes
from app.app_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    register_routes(app)
    return app

app = create_app()