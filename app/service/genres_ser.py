from app.dao.genres_dao import GenresDAO


class GenresService:
    def __init__(self, dao: GenresDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        gid = data.get("id")

        genre = self.get_one(gid)

        genre.name = data.get('name')

        return self.dao.update(genre)

    def update_patch(self, data):
        gid = data.get("id")

        genre = self.get_one(gid)

        if 'name' in genre:
            genre.name = data.get('name')

        return self.dao.update(genre)

    def delete(self, gid):
        self.dao.delete(gid)