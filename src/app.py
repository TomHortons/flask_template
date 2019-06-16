from . import create_app
from flask_restful import Resource


app, api = create_app()


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True)
