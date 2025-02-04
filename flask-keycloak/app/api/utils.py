
from logger import logger
from flask import request

def before_request():
    logger.debug('Before request is called')
    auth_header = request.headers.get('Authorization')
    if auth_header:
        logger.debug(f'Authorization header: {auth_header}')