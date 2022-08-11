from dao import DirectorDAO
from dao.model.director_model import Director


class DirectorService:
    """
    Service for Director objects
    """
    def __init__(self, director_dao: DirectorDAO):
        self.dao: DirectorDAO = director_dao

    def get_all_directors(self) -> Director:
        return self.dao.select_all_items()

    def get_director_by_id(self, did: int) -> Director | None:
        if self.dao.select_item_by_pk(did):
            return self.dao.select_item_by_pk(did)
        return None
