import jwt

from api import app, db

from functools import wraps
from flask import abort, request

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if not 'Authorization' in request.headers:
            app.logger.error('Authorization missing in request headers')
            abort(401)
        try:
            auth_header = request.headers.get('Authorization')
            auth_token = auth_header.split(" ")[1]
            app.logger.info('Auth Token:{}'.format(auth_token))
            payload = jwt.decode(auth_token, app.config.get('JWT_SECRET_KEY'))
            if not payload.get('user_id'):
                app.logger.error('Permission Denied for token:{}'.format(auth_token))
                abort(400, 'Permission Denied to access')

        except jwt.ExpiredSignatureError:
            app.logger.error('Signature expired. Please log in again.')
            return 'Signature expired. Please log in again.'
        except  jwt.InvalidTokenError:
            app.logger.error('Invalid token. Please log in again.')
            return 'Invalid token. Please log in again.'

        return f(payload, *args, **kws)
    return decorated_function