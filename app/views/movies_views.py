from flask import request
from flask_restx import Resource, Namespace

from app.container import movies_service
from app.dao.model.movies import MovieSchema



movies_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        # director_id = request.values.get("director_id")
        # genre_id = request.values.get("genre_id")
        #
        #
        # if director_id and genre_id:
        #     movies_by_director_genre = db.session.query(Movie).filter(Movie.director_id == director_id , Movie.genre_id == genre_id).all()
        #     return movies_schema.dump(movies_by_director_genre), 200
        # elif genre_id:
        #     movies_by_genre = db.session.query(Movie).filter(Movie.genre_id == genre_id).all()
        #     return movies_schema.dump(movies_by_genre), 200
        # elif director_id:
        #     movies_by_director = db.session.query(Movie).filter(Movie.director_id == director_id).all()
        #     return movies_schema.dump(movies_by_director), 200

        all_movies = movies_service.get_all()
        return movies_schema.dump(all_movies), 200


    def post(self):
        req_json = request.json
        movies_service.create(req_json)
        return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movies_service.get_one(mid)
        if not movie:
            return "", 404
        return movie_schema.dump(movie), 200


    def put(self, mid):
        req_json = request.json
        req_json['id'] = mid

        movie = movies_service.update(req_json)
        return movie_schema.dump(movie), 204


    def patch(self, mid):
        req_json = request.json
        req_json['id'] = mid

        movies_service.update_patch(req_json)

        return "", 204

    def delete(self, mid):
        movies_service.delete(mid)

        return "", 204
