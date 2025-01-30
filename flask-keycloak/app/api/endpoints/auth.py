from flask import Blueprint, redirect, url_for

from app.services.oidc import oidc

blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@blueprint.route('/login')
def login():
    return oidc.redirect_to_auth_server(url_for('pages.index', _external=True))

@blueprint.route('/logout')
@oidc.require_login
def logout():
    oidc.logout()
    return redirect(url_for('pages.index'))