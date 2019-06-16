from flask import Flask
from flask_restful import Api

# from .models import db
# from . import config


def create_app():
    flask_app = Flask(__name__)
    # flask_app.config['SQLALCHEMY_DATABASE_URI']\
    #  = config.DATABASE_CONNECTION_URI
    # flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    # db.init_app(flask_app)
    # db.create_all()

    api = Api(flask_app)
    return flask_app, api
