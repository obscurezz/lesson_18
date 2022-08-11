from marshmallow import Schema, fields


class MovieModel(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()


class DirectorModel(Schema):
    id = fields.Int()
    name = fields.Str()


class GenreModel(Schema):
    id = fields.Int()
    name = fields.Str()
