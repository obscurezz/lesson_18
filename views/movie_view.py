from flask_restx import Resource, Namespace
from flask import request, jsonify

from dao.model.movie_model import Movie

from implemented import movie_service
from dao.model.models import MovieModel

from parsers import lateral_parser

movies_ns: Namespace = Namespace('movies', description='namespace for movies')

movie_model = MovieModel()
movies_model = MovieModel(many=True)


@movies_ns.route('/')
class AllMoviesView(Resource):
    """
    GET: implements GET-method for /movies
    POST: implements POST-method to add new object to database
    """
    @staticmethod
    def get():
        if not request.args.keys():
            all_movies: list[Movie] = movie_service.get_all_movies()
            return movies_model.dump(all_movies), 200
        else:
            try:
                query = {k: v for k, v in lateral_parser.parse_args().items() if v is not None}
                movies_by_query: list[Movie] = movie_service.get_movie_by_query(**query)
                return movies_model.dump(movies_by_query), 200
            except Exception as e:
                return jsonify({'Exception': e}), 500

    @staticmethod
    def post():
        request_body: dict = request.json
        movie_service.post_movie(**request_body)
        try:
            return "", 201, {'location': "/movies"}
        except Exception as e:
            return jsonify({'Exception': e}), 500


@movies_ns.route('/<int:mid>')
class SingleMovieView(Resource):
    """
    GET: implements GET-method for /movies/... where ... is ID of object
    PUT: implements PUT-method to fully update object in database
    DELETE: implements DELETE-method to delete object from database
    """
    @staticmethod
    def get(mid: int):
        current_movie: Movie = movie_service.get_movie_by_id(mid)
        try:
            return movie_model.dump(current_movie), 200
        except Exception as e:
            return jsonify({'Exception': e}), 500

    @staticmethod
    def put(mid: int):
        request_body: dict = request.json
        movie_service.put_movie(mid, **request_body)
        try:
            return "", 204
        except Exception as e:
            return jsonify({'Exception': e}), 500

    @staticmethod
    def delete(mid: int):
        movie_service.delete_movie(mid)
        try:
            return "", 204
        except Exception as e:
            return jsonify({'Exception': e}), 500
