# -*- coding: utf-8 -*- 
from flask import Flask
from flask.helpers import request, jsonify
import json

app = Flask(__name__)

FROM='from'
TO='to'
DEFAULT_COUNT=20


def cat_generator():
    u'''Генератор категорий и жанров'''
    genre_id=0;
    for cat_id in xrange(4):
        genres=[]
        while genre_id<(cat_id+1)*5:
            t=u'Жанр %s'%genre_id
            genres.append({'title':t,'id': genre_id}  )
            genre_id=genre_id+1
        yield {'title':u'Категория %s'%cat_id,'id':cat_id,'genres':genres }
        cat_id=cat_id+1
    

def promo_generator(promo_from=None, promo_to=None):
    u'''Генератор видео для промоблока'''
    video_id=0;
    num=0;
    if promo_from and promo_to and promo_to-promo_from > 100:
        promo_to=promo_from+100
    if not promo_from:
        promo_from=0
    if not promo_to:
        promo_to=promo_from+DEFAULT_COUNT
    while video_id<10:
        if (promo_from<=num<=promo_to) or (not promo_from and not promo_to):
            yield {'id':video_id,'title':'Video %s'%video_id,'Category_id':1,'Genre_id':1}
        video_id=video_id+1
        num=num+1




@app.route('/categories/')
def categories():
    u'''Получение списка всех рубрик  '''
    d=list(cat_generator())
    return json.dumps(d)

@app.route('/promo/')
def promo():
    u'''Получение списка видео из промоблока'''
    promo_from=None
    promo_to=None
    if FROM in request.args:
        promo_from=request.args.get(FROM, 0, type=int)
    if TO in request.args:
        promo_to=request.args.get(TO, 0, type=int)
    if (promo_from and promo_to) and promo_from>promo_to:
        return jsonify(error='parametr to less than parametr from')
    d=list(promo_generator(promo_from,promo_to))
    return json.dumps(d)


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b,method='_add_numbers',)


if __name__ == '__main__':
    app.run(debug=True)

    