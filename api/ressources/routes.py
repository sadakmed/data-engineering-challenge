from .api import NewsAPI
from flask_restful import Api

def initialize_routes(app):
    api = Api(app,prefix='/api/v1/news')
    api.add_resource(NewsAPI,'')