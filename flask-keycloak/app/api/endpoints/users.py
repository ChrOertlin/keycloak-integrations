from flask import Blueprint
from app.services.oidc import oidc

blueprint = Blueprint('users', __name__)

@blueprint.route('/users', methods=['GET'])
@oidc.accept_token(require_token=True)
def get_user():
    return {"message": "this is a user"}