from app.dao.model.director import Director


class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, data):
        director = Director(
        name = data.get('name')
        )
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, director):
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, did):
        director = self.get_one(did)

        self.session.delete(director)
        self.session.commit()
