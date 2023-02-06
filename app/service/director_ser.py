from app.dao.directors_dao import DirectorsDAO


class DirectorsService:
    def __init__(self, dao: DirectorsDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        did = data.get("id")
        director = self.get_one(did)
        director.name = data.get('name')
        return self.dao.update(director)




    def update_patch(self, data):
        did = data.get("id")

        director = self.get_one(did)

        if 'name' in director:
            director.name = data.get('name')

        return self.dao.update(director)


    def delete(self, did):
        self.dao.delete(did)