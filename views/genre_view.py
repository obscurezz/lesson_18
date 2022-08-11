from flask_restx import Resource, Namespace
from flask import jsonify

from dao.model.genre_model import Genre

from implemented import genre_service
from dao.model.models import GenreModel

genres_ns: Namespace = Namespace('directors', description='namespace for directors')

genre_model = GenreModel()
genres_model = GenreModel(many=True)


@genres_ns.route('/')
class AllGenresView(Resource):
    """
    GET: implements get request for all genres
    """
    @staticmethod
    def get():
        all_genres: list[Genre] = genre_service.get_all_directors()
        return genres_model.dump(all_genres), 200


@genres_ns.route('/<int:gid>')
class SingleGenreView(Resource):
    """
    GET: implements get request for exact genre by its id
    """
    @staticmethod
    def get(gid: int):
        current_genre: Genre = genre_service.get_director_by_id(gid)
        try:
            return genre_model.dump(current_genre)
        except Exception as e:
            return jsonify({'Exception': e}), 500
