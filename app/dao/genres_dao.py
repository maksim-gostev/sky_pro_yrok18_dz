from app.dao.model.genre import Genre


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.get(did)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        genre = Genre(name = data.get('name'))
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, gid):
        genre = self.get_one(gid)

        self.session.delete(genre)
        self.session.commit()
