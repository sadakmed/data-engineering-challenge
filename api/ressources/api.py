from flask import Response, request
from database.models import News
from flask_restful import Resource


class NewsAPI(Resource):
    
    def get(self):
        
        tag=request.args.get('tag',None)
        author=request.args.get('author',None)
        headline=request.args.get('headline',None)
        
        fdict = dict()
        if tag : fdict['topic__icontains']  = tag
        if author: fdict['author__icontains'] = author
        if headline: fdict['headline__icontains'] = headline
        print(fdict)
        news = News.objects.filter(**fdict).to_json()

        return Response(news, mimetype="application/json", status=200)



