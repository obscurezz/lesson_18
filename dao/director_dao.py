from sqlalchemy.orm import scoped_session
from dao.model.director_model import Director

from typing import Type


class DirectorDAO:
    """
    Data access for Director objects;
    db_session: gets database session
    model: SQLAlchemy model
    """
    def __init__(self, db_session: scoped_session):
        self.session: scoped_session = db_session
        self.__model__: Type[Director] = Director

    # select * from director
    def select_all_items(self):
        return self.session.query(self.__model__).all()

    # select * from director here id = ...
    def select_item_by_pk(self, pk: int):
        return self.session.query(self.__model__).get(pk)
