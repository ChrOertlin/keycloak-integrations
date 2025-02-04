from http import HTTPStatus
from app.logger import logger
from flask import request, jsonify
from app.services.oidc import keycloak_openid
from keycloak.exceptions import KeycloakError

def before_request():
    logger.debug('Before request is called')
    auth_header = request.headers.get('Authorization')
    logger.debug(f'Authorization header: {auth_header}')
    if request.method == 'OPTIONS':
        return
    
    if not auth_header:
        logger.debug('No Authorization header found')
        return jsonify({'message': 'No authorization header'}), HTTPStatus.UNAUTHORIZED
    
    try:
        token = auth_header.split(" ")[1]
        token_info = keycloak_openid.introspect(token)
        
        if not token_info['active']:
            logger.debug('Token is not active')
            return jsonify({'message': 'Invalid token'}), HTTPStatus.UNAUTHORIZED
        
        verified_token = keycloak_openid.decode_token(token)
        logger.debug(f"Token verified user is {verified_token.get('name')}")
    
    except KeycloakError as e:
        logger.error(f"Error during token verification: {e}")
        return jsonify({'message': 'Invalid token'}), HTTPStatus.UNAUTHORIZED
    except Exception as e:
        logger.error(f"Unexpected error during token verification: {e}")
        return jsonify({'message': 'Internal server error'}), HTTPStatus.INTERNAL_SERVER_ERROR