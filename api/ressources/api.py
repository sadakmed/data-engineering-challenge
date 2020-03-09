from itertools import chain
from flask import Response, request, jsonify
from database.models import News
from flask_restful import Resource
from bson.objectid import ObjectId
import json



class NewsPnt(Resource):
    
    def get(self):
        
        tag=request.args.get('tag',None)
        author=request.args.get('author',None)
        headline=request.args.get('headline',None)
        
        fdict = dict()
        if tag : fdict['tag__icontains']  = tag
        if author: fdict['authors'] = author
        if headline: fdict['headline__icontains'] = headline
        print(fdict)
        news = News.objects.filter(**fdict).exclude('article','date').to_json()

        return Response(news, mimetype="application/json", status=200)



class ArticlePnt(Resource):
    def get(self,id):
        news = News.objects.filter(id = ObjectId(id)).to_json()
        return Response(news, mimetype="application/json", status=200)


class AuthorPnt(Resource):
    def get(self):
        news = News.objects.only('authors')
        authors=list(map( lambda x:x['authors'],json.loads(news.to_json())))
        y = set(chain(*authors))
        return jsonify({'authors':list(y)})

class TagPnt(Resource):
    def get(self):
        news = News.objects.only('tag').distinct('tag')
        print(news)
        return jsonify({'tags':news})

        