from flask_bootstrap import Bootstrap4
from flask import Flask
from flask_cors import CORS
import logging

app = Flask('details')
app.config.from_pyfile('config.py')
CORS(app)

bootstrap = Bootstrap4(app)

logger = logging.getLogger('gunicorn.access')

from details.views import backend,login
from details.api_v1 import api_v1

app.register_blueprint(api_v1, url_prefix = '/api')