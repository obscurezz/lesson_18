from dao import MovieDAO
from dao.model.movie_model import Movie


class MovieService:
    """
    Service for Movie objects
    """
    def __init__(self, movie_dao: MovieDAO):
        self.dao: MovieDAO = movie_dao

    def get_all_movies(self) -> list[Movie]:
        return self.dao.select_all_items()

    def get_movie_by_id(self, mid: int) -> Movie | None:
        if self.dao.select_item_by_pk(mid):
            return self.dao.select_item_by_pk(mid)
        return None

    # def get_movie_by_query(self, **kwargs) -> list[Movie]:
    #     # did: int | None = None, gid: int | None = None, year: int | None = None
    #     if not kwargs:
    #         return self.get_all_movies()
    #     elif 'director_id' in kwargs.keys():
    #         return self.dao.select_items_by_director_id(kwargs['director_id'])
    #     elif 'genre_id' in kwargs.keys():
    #         return self.dao.select_items_by_genre_id(kwargs['genre_id'])
    #     elif 'year' in kwargs.keys():
    #         return self.dao.select_items_by_year(kwargs['year'])

    def get_movie_by_query(self, **kwargs) -> list[Movie]:
        if not kwargs:
            return self.get_all_movies()
        else:
            return self.dao.select_items_by_arguments(**kwargs)

    def post_movie(self, **kwargs) -> Movie:
        new_item: Movie = self.dao.insert_item(**kwargs)
        return new_item

    def put_movie(self, mid: int, **kwargs) -> Movie:
        update_item: Movie = self.dao.update_item_by_pk(mid, **kwargs)
        return update_item

    def delete_movie(self, mid: int) -> Movie:
        delete_item: Movie = self.dao.delete_item_by_pk(mid)
        return delete_item
