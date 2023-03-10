from flask import request
from flask_restx import Resource, Namespace

from app.container import directors_service
from app.dao.model.director import DirectorSchema

directors_ns = Namespace('director')

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()

@directors_ns.route('')
class DirectorsView(Resource):
    def get(swlf):
        all_derector = directors_service.get_all()
        return directors_schema.dump(all_derector)


    def post(self):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404
        director = directors_service.create(req_json)
        return director_schema.dump(director), 201



@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = directors_service.get_one(did)
        if not director:
            return "такого режисёра нет", 404
        return director_schema.dump(director), 201


    def put(self, did):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404

        req_json['id'] = did

        director = directors_service.update(req_json)
        return director_schema.dump(director), 204


    def delete(self, did):
        directors_service.delete(did)
        return "", 204




    def patch(self, did):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404

        req_json['id'] = did

        director = directors_service.patch(req_json)
        return director_schema.dump(director), 204





