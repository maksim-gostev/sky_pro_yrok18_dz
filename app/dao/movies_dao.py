from app.dao.model.movies import Movie


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(
        title = data.get('title'),
        description = data.get('description'),
        trailer = data.get('trailer'),
        year = data.get('year'),
        rating = data.get('rating'),
        genre_id = data.get('genre_id'),
        director_id = data.get('director_id'),
        genre = data.get('genre'),
        director = data.get('director')
        )
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
