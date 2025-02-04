from flask import Blueprint
blueprint = Blueprint('users', __name__,url_prefix='/users')

@blueprint.route('/get_user', methods=['GET'])
def get_user():
    """This endpoint is for testing purposes and just returns a dummy user."""
    return {"user": "Test User"}