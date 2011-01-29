# -*- coding: utf-8 -*- 
from flask import Flask
from flask.helpers import request, jsonify
import json

app = Flask(__name__)


def cat_generator():
    '''Генератор категорий и жанров'''
    cat_id=0;
    genre_id=0;
    while cat_id<4:
        genres=[]
        while genre_id<(cat_id+1)*5:
            t='Genre %s'%genre_id
            genres.append({'title':t,'id': genre_id}  )
            genre_id=genre_id+1
        yield {'title':'Category %s'%cat_id,'id':cat_id,'genres':genres }
        cat_id=cat_id+1
    

def promo_generator(promo_from=None, promo_to=None):
    '''Генератор видео для промоблока'''
    video_id=0;
    num=0;
    while video_id<10:
        if (promo_from<=num<=promo_to) or (promo_from==None and promo_to==None):
            yield {'id':video_id,'title':'Video %s'%video_id,'Category_id':1,'Genre_id':1}
        video_id=video_id+1
        num=num+1

@app.route('/categories/')
def categories():
    u"""Получение списка всех рубрик  """
    d=list(cat_generator())
    print d
    return '%s'%d

@app.route('/promo/')
def promo():
    u"""Получение списка видео из промоблока  """
    promo_from=request.args.get('from', 0, type=int)
    promo_to=request.args.get('to', 0, type=int)
    if promo_from>promo_to:
        return jsonify(error='parametr to less than parametr from')
    if promo_to-promo_from > 100:
        promo_to=promo_from+100
    d=list(promo_generator(promo_from,promo_to))
    print d
    return '%s'%d


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b,method='_add_numbers',)


if __name__ == '__main__':
    app.run(debug=True)

    