import os


class Config:
    OIDC_CLIENT_SECRETS = 'client_secrets.json'
    OIDC_SCOPES = ['openid', 'email', 'profile']
    OIDC_TOKEN_TYPE_HINT = 'access_token'
    SECRET_KEY = "very-secret-password"
    OIDC_ID_TOKEN_COOKIE_SECURE: False
    OIDC_COOKIE_SECURE: False
    OIDC_REQUIRE_VERIFIED_EMAIL: False
    OIDC_USER_INFO_ENABLED: True
    OIDC_OPENID_REALM: 'flask-client'
    OIDC_INTROSPECTION_AUTH_METHOD: 'client_secret_post'
    OIDC_RESOURCE_CHECK_AUD: True #Audience
    OIDC_CLOCK_SKEW: 560 #iat must be > time.time() - OIDC_CLOCK_SKEW