import os


class Config:
    OIDC_CLIENT_SECRETS = os.getenv('OIDC_CLIENT_SECRETS', 'keycloak_config.json')
    OIDC_SCOPES = ['openid', 'email', 'profile']
    OIDC_TOKEN_TYPE_HINT = 'access_token'
    SECRET_KEY = "supersecretkey"
