from dao import GenreDAO
from dao.model.genre_model import Genre


class GenreService:
    """
    Service for Genre objects
    """
    def __init__(self, genre_dao: GenreDAO):
        self.dao: GenreDAO = genre_dao

    def get_all_genres(self) -> Genre:
        return self.dao.select_all_items()

    def get_genre_by_id(self, gid: int) -> Genre | None:
        if self.dao.select_item_by_pk(gid):
            return self.dao.select_item_by_pk(gid)
        return None
