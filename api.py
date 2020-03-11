from flask import Flask, jsonify, json
from flask_cors import CORS, cross_origin
from flask_restful import reqparse, abort, Api, Resource
from flask import request

from models import Person
from database import Database

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
parser = reqparse.RequestParser()

# ElevesList
class Eleve(Resource):
    def __init__(self):
        self.db = Database()

    def delete(self, eleve_id):
        self.db.delete(eleve_id)

    def put(self, eleve_id):
        data = request.get_json()
        self.db.update(eleve_id, data)


class ElevesList(Resource):
    def __init__(self):
        self.db = Database()

    def get(self):
        return jsonify(self.db.list_eleves())

    def post(self):
        data = request.get_json()
        self.db.insert(data)

##
## Actually setup the Api resource routing here
##
api.add_resource(ElevesList, '/eleves')
api.add_resource(Eleve, '/eleves/<eleve_id>')


if __name__ == '__main__':
    app.run(debug=True)
