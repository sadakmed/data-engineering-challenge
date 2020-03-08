from flask import Response, request, jsonify
from database.models import News
from flask_restful import Resource
from bson.objectid import ObjectId
import json


class NewsAPI(Resource):
    
    def get(self):
        
        tag=request.args.get('tag',None)
        author=request.args.get('author',None)
        headline=request.args.get('headline',None)
        
        fdict = dict()
        if tag : fdict['tag__icontains']  = tag
        if author: fdict['author__icontains'] = author
        if headline: fdict['headline__icontains'] = headline
        print(fdict)
        news = News.objects.filter(**fdict).to_json()

        return Response(news, mimetype="application/json", status=200)



class ArticleAPI(Resource):
    def get(self,id):
        news = News.objects.filter(id = ObjectId(id)).to_json()
        return Response(news, mimetype="application/json", status=200)



class AuthorAPI(Resource):
    def get(self):
        news = News.objects.only('author')
        authors=list(map( lambda x:x['author'],json.loads(news.to_json())))
        return jsonify({'authors':authors})

class TagAPI(Resource):
    def get(self):
        news = News.objects.only('tag')
        tag=list(map( lambda x:x['tag'],json.loads(news.to_json())))
        return jsonify({'tags':tag})

        