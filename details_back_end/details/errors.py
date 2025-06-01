from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

from details import app

def api_abort(code, message=None, **kwargs):
    if message is None:
        message = HTTP_STATUS_CODES.get(code, '')

    response = jsonify(code=code, message=message, **kwargs)
    response.status_code = code
    return response  # You can also just return (response, code) tuple


def invalid_token():
    response = api_abort(401, error='invalid_token', error_description='Either the token was expired or invalid.')
    return response


def token_missing():
    response = api_abort(401,"fail to get token")
    return response


class ValidationError(ValueError):
    pass


@app.errorhandler(ValidationError)
def validation_error(e):
    return api_abort(400, e.args[0])
