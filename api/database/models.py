from .db import db

class News(db.Document):
    headline=db.StringField()
    author=db.StringField()
    topic=db.StringField()
    url=db.StringField()
    date=db.DateTimeField()
    imgs=db.ListField(db.StringField())
    article=db.StringField()