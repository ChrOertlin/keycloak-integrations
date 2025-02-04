from app.api.endpoints.auth import blueprint as auth_blueprint
from app.api.endpoints.users import blueprint as users_blueprint
from app.api.views.pages import blueprint as pages_blueprint

def register_routes(app) -> None:
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(pages_blueprint)
