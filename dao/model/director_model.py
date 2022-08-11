from dao.model.base_model import Base
from setup_db import db


class Director(Base):
    __tablename__ = 'director'

    name = db.Column(db.String(255), unique=True)
