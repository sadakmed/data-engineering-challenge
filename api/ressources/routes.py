from .api import NewsAPI , ArticleAPI,AuthorAPI,TagAPI
from flask_restful import Api

def initialize_routes(app):
    api = Api(app,prefix='/api/v1/news')
    api.add_resource(NewsAPI,'')
    api.add_resource(ArticleAPI,'/<id>')
    api.add_resource(AuthorAPI,'/author')
    api.add_resource(TagAPI,'/tag')