from flask import Flask
from flask_cors import CORS
from app.api.routes import register_routes
from app.app_config import Config
from app.services.oidc import oidc

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    oidc.init_app(app)
    
    @app.context_processor
    def inject_oidc():
        return dict(oidc=oidc)
    
    register_routes(app)
    return app

app = create_app()