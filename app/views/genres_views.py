from flask import request
from flask_restx import Resource, Namespace

from app.container import genres_service
from app.dao.model.genre import GenreSchema



genres_ns = Namespace('genre')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genres_ns.route('')
class  GenresView(Resource):
    def get(self):
        genre = genres_service.get_all()
        return genres_schema.dump(genre)

    def post(self):
        req_json = request.json
        genre = genres_service.create(req_json)
        return genre_schema.dump(genre), 201


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genres_service.get_one(gid)
        return genre_schema.dump(genre), 201


    def put(self, gid):
        req_json = request.json
        req_json['id'] = gid

        genre = genres_service.update(req_json)
        return genre_schema.dump(genre), 204


    def delete(self, gid):
        genres_service.delete(gid)
        return "", 204
