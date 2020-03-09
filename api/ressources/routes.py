from .api import NewsPnt , ArticlePnt,AuthorPnt,TagPnt
from flask_restful import Api

def initialize_routes(app):
    api = Api(app,prefix='/api/v1/news')
    api.add_resource(NewsPnt,'')
    api.add_resource(ArticlePnt,'/<id>')
    api.add_resource(AuthorPnt,'/author')
    api.add_resource(TagPnt,'/tag')