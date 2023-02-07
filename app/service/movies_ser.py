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
        movie.director_id = data.get('director_id')

        return self.dao.update(movie)


    def delete(self, mid):
        self.dao.delete(mid)