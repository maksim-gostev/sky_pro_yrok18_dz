from app.dao.movies_dao import MoviesDAO


class MoviesService:
    def __init__(self, dao: MoviesDAO):
        self.dao = dao


    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()


    def create(self, data):
        return self.dao.create(data)


    def update(self, data):
        mid = data.get("id")

        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.genre = data.get('genre')
        movie.director_id = data.get('director_id')
        movie.director = data.get('director')

        return self.dao.update(movie)


    def update_patch(self, data):
        mid = data.get("id")

        movie = self.get_one(mid)

        if 'title' in movie:
            movie.title = data.get('title')
        if 'description' in movie:
            movie.description = data.get('description')
        if 'trailer' in movie:
            movie.trailer = data.get('trailer')
        if 'year' in movie:
            movie.year = data.get('year')
        if 'rating' in movie:
            movie.rating = data.get('rating')
        if 'genre_id' in movie:
            movie.genre_id = data.get('genre_id')
        if 'genre' in movie:
            movie.genre = data.get('genre')
        if 'director_id' in movie:
            movie.director_id = data.get('director_id')
        if 'director' in movie:
            movie.director = data.get('director')

        return self.dao.update(movie)


    def delete(self, mid):
        self.dao.delete(mid)