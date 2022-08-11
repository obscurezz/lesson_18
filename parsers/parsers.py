from flask_restx.reqparse import RequestParser

lateral_parser: RequestParser = RequestParser()
lateral_parser.add_argument(name='director_id', type=int, required=False, nullable=False)
lateral_parser.add_argument(name='genre_id', type=int, required=False, nullable=False)
lateral_parser.add_argument(name='year', type=int, required=False, nullable=False)
