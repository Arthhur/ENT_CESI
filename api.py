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

    def get(self, eleve_id):
        return jsonify(self.db.eleve_by_id(eleve_id))

    def delete(self, eleve_id):
        self.db.delete(eleve_id)

    def put(self, eleve_id):
        data = request.get_json()
        self.db.update(eleve_id, data)

    def post(self, eleve_id):
        data = request.get_json()
        self.db.insert(eleve_id, data)

class ElevesList(Resource):
    def __init__(self):
        self.db = Database()

    def get(self):
        return jsonify(self.db.list_eleves())

    def post(self):
        data = request.get_json()
        self.db.insert(data)

# IntervenantsList
class Intervenant(Resource):
    def __init__(self):
        self.db = Database()

    def get(self, intervenant_id):
        return jsonify(self.db.intervenant_by_id(intervenant_id))

    def delete(self, intervenant_id):
        self.db.intervenant_delete(intervenant_id)

    def put(self, intervenant_id):
        data = request.get_json()
        self.db.intervenant_update(intervenant_id, data)

    def post(self):
        data = request.get_json()
        self.db.intervenant_insert(data)


class IntervenantsList(Resource):
    def __init__(self):
        self.db = Database()

    def get(self):
        return jsonify(self.db.list_intervenants())

    def post(self):
        data = request.get_json()
        self.db.insert(data)

# Articles / Blog
class Blog(Resource):
    def __init__(self):
        self.db = Database()

    def get(self):
        return jsonify(self.db.blog())

    def post(self):
        data = request.get_json()
        return jsonify(self.db.insert(data))


class Article(Resource):
    def __init__(self):
        self.db = Database()

    def delete(self, article_id):
        self.db.delete(article_id)

    def put(self, article_id):
        data = request.get_json()
        self.db.update(article_id, data)


# Promotions
class Promotion(Resource):
    def __init__(self):
        self.db = Database()

    def get(self, promotion_id):
        return jsonify(self.db.promotion_by_id(promotion_id))

    def delete(self, promotion_id):
        self.db.promotion_delete(promotion_id)

    def put(self, promotion_id):
        data = request.get_json()
        self.db.promotion_update(id, data)

    def post(self, promotion):
        data = request.get_json()
        self.db.promotion_insert(self, promotion)


class PromotionList(Resource):
    def __init__(self):
        self.db = Database()

    def get(self):
        return jsonify(self.db.list_promotions())

    def post(self):
        data = request.get_json()
        self.db.promotion_insert(data)


class EdtList(Resource):
    def __init__(self):
        self.db = Database()

    def get(self):
        return jsonify(self.db.list_edt())

class Edt(Resource):
    def __init__(self):
        self.db = Database()

    def get(self, date):
        return jsonify(self.db.edt_by_day(date))

    def delete(self, edt_id):
        self.db.edt_delete(edt_id)

    def put(self, edt_id):
        data = request.get_json()
        self.db.edt_update(edt_id, data)

    def post(self, edt):
        data = request.get_json()
        self.db.edt_insert(self, edt)

class Auth(Resource):
    def __init__(self):
        self.db = Database()

    def post(self):
        data = request.get_json()
        return jsonify(self.db.auth(data))
##
## Actually setup the Api resource routing here
##
api.add_resource(ElevesList, '/eleves')
api.add_resource(Eleve, '/eleves/<eleve_id>')
## route intervenants
api.add_resource(IntervenantsList, '/intervenants')
api.add_resource(Intervenant, '/intervenants/<intervenant_id>')
## route promotions
api.add_resource(PromotionList, '/promotions')
api.add_resource(Promotion, '/promotions/<promotion_id>')
## route article
api.add_resource(Blog, '/blogs')
api.add_resource(Article, '/blog/<article_id>')
## route authentification
api.add_resource(Auth, '/auth')


if __name__ == '__main__':
    app.run(debug=True)
