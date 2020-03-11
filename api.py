from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import reqparse, abort, Api, Resource
from models import Person
from database import Database

app = Flask(__name__)
api = Api(app)

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class ElevesList(Resource):
    def get(self):
        db = Database()
        return jsonify(db.list_eleves())


##
## Actually setup the Api resource routing here
##
api.add_resource(ElevesList, '/eleves')

if __name__ == '__main__':
    app.run(debug=True)
