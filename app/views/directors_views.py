from flask import request
from flask_restx import Resource, Namespace

from app.container import directors_service
from app.dao.model.director import DirectorSchema

directors_ns = Namespace('director')

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


def get():
    all_derector = directors_service.get_all()
    return directors_schema.dump(all_derector)


def post():
    req_json = request.json
    director = directors_service.create(req_json)
    return director_schema.dump(director), 201


@directors_ns.route('')
class DirectorsView(Resource):
    pass


def patch(did):
    req_json = request.json
    req_json['id'] = did

    genre = directors_service.update_patch(req_json)

    return director_schema.dump(genre), 204


def delete(did):
    directors_service.delete(did)
    return "", 204


def put(did):
    req_json = request.json
    req_json['id'] = did
    director = directors_service.update(req_json)
    return director_schema.dump(director), 204


def get(gid):
    director = directors_service.get_one(gid)
    return director_schema.dump(director), 201


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    pass
