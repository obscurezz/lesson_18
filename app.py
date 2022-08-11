from typing import Type

from flask import Flask

from config import DevConfig, ProdConfig
from init_db import create_data
from setup_db import db
from views import api


def create_app(config_object: Type[DevConfig] | Type[ProdConfig]) -> Flask:
    """
    returns Flask application with set up parameters
    """
    app: Flask = Flask(__name__)
    app.config.from_object(config_object)
    app.app_context().push()
    db.init_app(app)

    with app.app_context():
        create_data(db)

    api.init_app(app)

    for item in app.config:
        print(f'{item}: {app.config[item]}')

    return app


if __name__ == '__main__':
    app = create_app(DevConfig)
    app.run(use_reloader=False)
