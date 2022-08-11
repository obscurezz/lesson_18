from sqlalchemy.orm import scoped_session
from dao.model.movie_model import Movie

from typing import Type


class MovieDAO:
    """
    Data access for Movie objects;
    db_session: gets database session
    model: SQLAlchemy model
    """
    def __init__(self, db_session: scoped_session):
        self.session: scoped_session = db_session
        self.__model__: Type[Movie] = Movie

    # select * from movie;
    def select_all_items(self):
        return self.session.query(self.__model__).all()

    # select * from movie where id = ...
    def select_item_by_pk(self, pk: int):
        return self.session.query(self.__model__).get(pk)

    # def select_items_by_director_id(self, director_id: int):
    #     return self.session.query(self.__model__).filter_by(self.__model__.director_id == director_id)
    #
    # def select_items_by_genre_id(self, genre_id: int):
    #     return self.session.query(self.__model__).filter_by(self.__model__.genre_id == genre_id)
    #
    # def select_items_by_year(self, year: int):
    #     return self.session.query(self.__model__).filter_by(self.__model__.year == year)

    # select * from movie where arg1 = ... and ...
    def select_items_by_arguments(self, **kwargs):
        return self.session.query(self.__model__).filter_by(**kwargs)

    # insert into movie ...
    def insert_item(self, **kwargs):
        new_item: Movie = self.__model__(**kwargs)
        self.session.add(new_item)
        self.session.commit()

        return new_item

    # update movie set ... where id = ...
    def update_item_by_pk(self, pk: int, **kwargs):
        update_item: Type[Movie] = self.session.query(self.__model__).get(pk)

        for k, v in kwargs.items():
            setattr(update_item, k, v)

        self.session.add(update_item)
        self.session.commit()

        return update_item

    # delete from movie where id = ...
    def delete_item_by_pk(self, pk: int):
        delete_item: Type[Movie] = self.session.query(self.__model__).get(pk)

        self.session.delete(delete_item)
        self.session.commit()

        return delete_item
