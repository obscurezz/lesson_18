from flask_restx import Api

from .movie_view import movies_ns
from .genre_view import genres_ns
from .director_view import directors_ns


api = Api(
    title='Lesson18_API',
    version='1.0',
    description='All namespaces of project into one API'
)

api.add_namespace(movies_ns)
api.add_namespace(genres_ns)
api.add_namespace(directors_ns)
