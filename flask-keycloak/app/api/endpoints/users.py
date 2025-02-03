from flask import Blueprint
blueprint = Blueprint('users', __name__)

@blueprint.route('/users', methods=['GET'])
def get_user():
    return {"message": "this is a user"}