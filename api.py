# -*- coding: utf-8 -*-
import string
from flask import Flask
from flask.helpers import request, jsonify
from functools import wraps
import json


app = Flask(__name__)

FROM='from'
TO='to'
DEFAULT_COUNT=20
MAX_COUNT=100
SORT_POP='pop'
SORT_NEW='new'


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
    

def video_list_generator(get_from=None, get_to=None, sort=SORT_POP, category=None,genre=None ):
    u'''Генератор видео для промоблока'''
    video_id=0;
    num=0;
    if not category:
        category=1
    if not genre:
        genre=1
    for video_id in xrange(get_from,get_to+1):
        if num<=MAX_COUNT:
            yield {'id':video_id,'thumbnail':u'http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg', 'title':'Video %s'%video_id,'categories':[category],'genres':[genre],'compilation':'Comedy Club','descrtiption':u'Очень смешно' }
        else:
            break
        num=num+1
        



def templated(template=None):
    u'''Декоратор для функций API'''
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):

            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            return json.dumps(ctx)
        return decorated_function
    return decorator




@app.route('/categories/')
@templated()
def categories():
    u'''Получение списка всех рубрик  '''
    d=list(cat_generator())
    return d

def from_to_check(args):
    u'''Единообразный обработчик границ листания списка видео'''
    get_from=None
    get_to=None
    if FROM in args:
        get_from=args.get(FROM, 0, type=int)
    if TO in request.args:
        get_to=args.get(TO, 0, type=int)
    if (get_from and get_to) and get_from>get_to:
        raise NameError("to_less_then_from")
    if get_from and get_to and get_to-get_from > MAX_COUNT:
        get_to=get_from+MAX_COUNT-1
    if not get_from:
        get_from=0
    if not get_to:
        get_to=get_from+DEFAULT_COUNT-1
    return [get_from,get_to]




@app.route('/promo/')
@templated()
def promo():
    u'''Получение списка видео из промоблока'''
    try:
        res=from_to_check(request.args)
        d=list(video_list_generator(res[0],res[1]))
    except NameError:
        d={'error':'parameter to less than parameter from'}
    return d


@app.route('/videos/')
@templated()
def videos():
    u'''Получение списка видео. Сортировка по новизне, фильтрация по категориям и рубрикам'''
    try:
        res=from_to_check(request.args)
        sort=request.args.get('sort', SORT_POP)
        category=request.args.get('category', None,type=int)
        genre=request.args.get('genre', None, type=int)
        if genre and category:
            d={'error':'only one filter parameter can be selected'}
        else:
            d=list(video_list_generator(res[0],res[1],sort,category, genre))
    except NameError:
        d={'error':'parametr to less than parametr from'}
    return d




if __name__ == '__main__':
    app.run(debug=True)

    