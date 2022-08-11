from dao import MovieDAO, GenreDAO, DirectorDAO
from service import MovieService, GenreService, DirectorService
from setup_db import db

movie_dao = MovieDAO(db_session=db.session)
movie_service = MovieService(movie_dao=movie_dao)

genre_dao = GenreDAO(db_session=db.session)
genre_service = GenreService(genre_dao=genre_dao)

director_dao = DirectorDAO(db_session=db.session)
director_service = DirectorService(director_dao=director_dao)
