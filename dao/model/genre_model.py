from dao.model.base_model import Base
from setup_db import db


class Genre(Base):
    __tablename__ = 'genre'

    name = db.Column(db.String(255), unique=True)
