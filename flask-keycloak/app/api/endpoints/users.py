from flask import Blueprint
from app.api.utils import before_request

blueprint = Blueprint('users', __name__,url_prefix='/users')
blueprint.before_request(before_request)


@blueprint.route('/get_user', methods=['GET'])
def get_user():
    """This endpoint is for testing purposes and just returns a dummy user."""
    return {"user": "Test User"}