import json
from constants import DATA_JSON
from flask_sqlalchemy import SQLAlchemy

from dao.model.genre_model import Genre
from dao.model.director_model import Director
from dao.model.movie_model import Movie


def create_data(db: SQLAlchemy) -> None:
    """
    db: database object for initialized app
    """
    db.drop_all()
    db.create_all()

    with open(DATA_JSON, 'r', encoding='utf-8') as jsonfile:
        init_data = json.load(jsonfile)

        for movie in init_data["movies"]:
            m = Movie(
                id=movie["pk"],
                title=movie["title"],
                description=movie["description"],
                trailer=movie["trailer"],
                year=movie["year"],
                rating=movie["rating"],
                genre_id=movie["genre_id"],
                director_id=movie["director_id"],
            )
            with db.session.begin():
                db.session.add(m)
                db.session.commit()

        for director in init_data["directors"]:
            d = Director(
                id=director["pk"],
                name=director["name"],
            )
            with db.session.begin():
                db.session.add(d)
                db.session.commit()

        for genre in init_data["genres"]:
            g = Genre(
                id=genre["pk"],
                name=genre["name"],
            )
            with db.session.begin():
                db.session.add(g)
                db.session.commit()
