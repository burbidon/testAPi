# -*- coding: utf-8 -*- 
__author__ = 'eross'

import api
import unittest
import json



class APITestCase(unittest.TestCase):

    def setUp(self):
         self.app = api.app.test_client()

    def tearDown(self):
        pass

#!!!!!!!!!!!!!!!!!!!!!!!!!Categories!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def test_categories(self):
        rv = self.app.get('/categories/')
        res=json.loads(rv.data)
        res_et=[{u'genres': [{u'id': 0, u'title': u'\u0416\u0430\u043d\u0440 0'}, {u'id': 1, u'title': u'\u0416\u0430\u043d\u0440 1'}, {u'id': 2, u'title': u'\u0416\u0430\u043d\u0440 2'}, {u'id': 3, u'title': u'\u0416\u0430\u043d\u0440 3'}, {u'id': 4, u'title': u'\u0416\u0430\u043d\u0440 4'}], u'id': 0, u'title': u'\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f 0'}, {u'genres': [{u'id': 5, u'title': u'\u0416\u0430\u043d\u0440 5'}, {u'id': 6, u'title': u'\u0416\u0430\u043d\u0440 6'}, {u'id': 7, u'title': u'\u0416\u0430\u043d\u0440 7'}, {u'id': 8, u'title': u'\u0416\u0430\u043d\u0440 8'}, {u'id': 9, u'title': u'\u0416\u0430\u043d\u0440 9'}], u'id': 1, u'title': u'\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f 1'}, {u'genres': [{u'id': 10, u'title': u'\u0416\u0430\u043d\u0440 10'}, {u'id': 11, u'title': u'\u0416\u0430\u043d\u0440 11'}, {u'id': 12, u'title': u'\u0416\u0430\u043d\u0440 12'}, {u'id': 13, u'title': u'\u0416\u0430\u043d\u0440 13'}, {u'id': 14, u'title': u'\u0416\u0430\u043d\u0440 14'}], u'id': 2, u'title': u'\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f 2'}, {u'genres': [{u'id': 15, u'title': u'\u0416\u0430\u043d\u0440 15'}, {u'id': 16, u'title': u'\u0416\u0430\u043d\u0440 16'}, {u'id': 17, u'title': u'\u0416\u0430\u043d\u0440 17'}, {u'id': 18, u'title': u'\u0416\u0430\u043d\u0440 18'}, {u'id': 19, u'title': u'\u0416\u0430\u043d\u0440 19'}], u'id': 3, u'title': u'\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f 3'}]
        assert len(res)==len(res_et)
        for i in res:
            assert i in res_et

#!!!!!!!!!!!!!!!!!!!!!!!!!Promo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def test_promo(self):
        rv = self.app.get('/promo/')
        res=json.loads(rv.data)
        assert len(res)==20 # Пока стоит такое ограничение на выдачу по умолчанию

    def test_promo_objects(self):
        rv = self.app.get('/promo/?from=0&to=3')
        res=json.loads(rv.data)
        res_et=[{u'genres': [1], u'title': u'Video 0', u'compilation': u'Comedy Club', u'thumbnail': u'http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg', u'descrtiption': u'\u041e\u0447\u0435\u043d\u044c \u0441\u043c\u0435\u0448\u043d\u043e', u'id': 0, u'categories': [1]}, {u'genres': [1], u'title': u'Video 1', u'compilation': u'Comedy Club', u'thumbnail': u'http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg', u'descrtiption': u'\u041e\u0447\u0435\u043d\u044c \u0441\u043c\u0435\u0448\u043d\u043e', u'id': 1, u'categories': [1]}, {u'genres': [1], u'title': u'Video 2', u'compilation': u'Comedy Club', u'thumbnail': u'http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg', u'descrtiption': u'\u041e\u0447\u0435\u043d\u044c \u0441\u043c\u0435\u0448\u043d\u043e', u'id': 2, u'categories': [1]}, {u'genres': [1], u'title': u'Video 3', u'compilation': u'Comedy Club', u'thumbnail': u'http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg', u'descrtiption': u'\u041e\u0447\u0435\u043d\u044c \u0441\u043c\u0435\u0448\u043d\u043e', u'id': 3, u'categories': [1]}]
        for i in res:
            assert i in res_et


    def test_promo_from_to(self):
        rv = self.app.get('/promo/?from=1&to=2')
        res=json.loads(rv.data)
        assert len(res)==2

    def test_promo_from_to100(self):
        rv = self.app.get('/promo/?from=5&to=150')
        res=json.loads(rv.data)
        assert len(res)==100


    def test_promo_from(self):
       rv = self.app.get('/promo/?from=1')
       res=json.loads(rv.data)
       assert len(res)==20

    def test_promo_to(self):
       rv = self.app.get('/promo/?to=1')
       res=json.loads(rv.data)
       assert len(res)==2

    def test_promo_to_from_error(self):
       rv = self.app.get('/promo/?from=10&to=1')
       assert 'error' in rv.data

    def test_promo_get_type_values(self):
       rv = self.app.get('/promo/?from=zopa&to=sisa')
       res=json.loads(rv.data)
       assert len(res)==20

    def test_videos_category_genre(self):
        rv = self.app.get('/videos/?category=5&genre=4')
        assert 'error' in rv.data


if __name__ == '__main__':
    unittest.main()