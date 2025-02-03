from flask import Flask, jsonify, request, redirect, session, Blueprint
from functools import wraps
from app.services.oidc import keycloak_openid

from app.logger import logger

blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@blueprint.route('/login')
def login():
    auth_url = keycloak_openid.auth_url(
        redirect_uri="http://localhost:3001/auth/callback",
        scope="openid profile email"
    )
    return redirect(auth_url)

@blueprint.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        token = keycloak_openid.token(
            grant_type='authorization_code',
            code=code,
            redirect_uri="http://localhost:3001/auth/callback"
        )
        session['token'] = token
        userinfo = keycloak_openid.userinfo(token['access_token'])
        session['userinfo'] = userinfo
        return redirect('/')
    return 'Authentication failed', 401

@blueprint.route('/logout')
def logout():
    token = session.get('token')
    if token:
        # Logout from Keycloak
        keycloak_openid.logout(token['refresh_token'])
    session.clear()
    return redirect('/')