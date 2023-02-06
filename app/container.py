from app.dao.directors_dao import DirectorsDAO
from app.dao.genres_dao import GenresDAO
from app.dao.movies_dao import MoviesDAO
from app.service.director_ser import DirectorsService
from app.service.genres_ser import GenresService
from app.service.movies_ser import MoviesService
from setup_db import db

movies_dao = MoviesDAO(db.session)
movies_service = MoviesService(movies_dao)

genres_dao = GenresDAO(db.session)
genres_service = GenresService(genres_dao)

directors_dao = DirectorsDAO(db.session)
directors_service = DirectorsService(directors_dao)