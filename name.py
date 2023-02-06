from flask import Flask
from flask_restx import Api

from app.views.directors_views import directors_ns
from app.views.genres_views import genres_ns
from app.views.movies_views import movies_ns
from config import Config
from setup_db import db



def create_app(config_object) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    return application


def configyre_app(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)



if __name__ == '__main__':
    app = create_app(Config())
    configyre_app(app)
    app.run()
