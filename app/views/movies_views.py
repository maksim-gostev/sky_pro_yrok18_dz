from flask import request
from flask_restx import Resource, Namespace

from app.container import movies_service
from app.dao.model.movies import MovieSchema



movies_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movies_ns.route('')
class MoviesView(Resource):
    def get(self):
        director_id = request.values.get("director_id")
        genre_id = request.values.get("genre_id")
        year = request.values.get("year")
        all_movies = movies_service.get_all(director_id, genre_id, year)
        return movies_schema.dump(all_movies), 200


    def post(self):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404
        movies_service.create(req_json)
        return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movies_service.get_one(mid)
        if not movie:
            return "такого фильма нет", 404
        return movie_schema.dump(movie), 200


    def put(self, mid):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404

        req_json['id'] = mid

        movie = movies_service.update(req_json)
        return movie_schema.dump(movie), 204


    def delete(self, mid):
        movies_service.delete(mid)

        return "", 204


    def patch(self, mid):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404

        req_json['id'] = mid

        movie = movies_service.patch(req_json)
        return movie_schema.dump(movie), 204
