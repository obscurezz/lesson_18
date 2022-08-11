from sqlalchemy.orm import scoped_session
from dao.model.genre_model import Genre

from typing import Type


class GenreDAO:
    """
    Data access for Genre objects;
    db_session: gets database session
    model: SQLAlchemy model
    """
    def __init__(self, db_session: scoped_session):
        self.session: scoped_session = db_session
        self.__model__: Type[Genre] = Genre

    # select * from genre
    def select_all_items(self):
        return self.session.query(self.__model__).all()

    # select * from genre where id = ...
    def select_item_by_pk(self, pk: int):
        return self.session.query(self.__model__).get(pk)
