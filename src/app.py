from flask import Flask
from flask_restful import Resource, Api


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


app, api = create_app()


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True)
