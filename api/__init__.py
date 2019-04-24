import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)

# Loading Settings
if os.environ.get('env_name') == 'dev':
    app.config.from_object('api.settings.Development')

elif os.environ.get('env_name') == 'staging':
    app.config.from_object('api.settings.Testing')

else:
    app.config.from_object('api.settings.Production')

api = Api(app)

db = SQLAlchemy(app)

from api.views import books

app.register_blueprint(books.books)
