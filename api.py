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


class ElevesList(Resource):
    def __init__(self):
        self.db = Database()

    def get(self):
        return jsonify(self.db.list_eleves())

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
        self.db.insert(data)


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

## EDT
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

    def put(self, id):
        data = request.get_json()
        self.db.edt_update(id, data)

    def post(self, edt):
        data = request.get_json()
        self.db.edt_insert(self, edt)

## FIN EDT
##
## Actually setup the Api resource routing here
##
api.add_resource(ElevesList, '/eleves')
api.add_resource(Eleve, '/eleves/<eleve_id>')
api.add_resource(PromotionList, '/promotions')
api.add_resource(Promotion, '/promotions/<promotion_id>')
## route article
api.add_resource(Blog, '/blog')
api.add_resource(Article, '/blog/<article_id>')

##  route edt
api.add_resource(EdtList, '/edt')
api.add_resource(Edt, '/edt/<date>')

if __name__ == '__main__':
    app.run(debug=True)
