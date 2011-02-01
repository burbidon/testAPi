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
        res_et=[{"Genre_id": 1, "title": "Video 0", "Category_id": 1, "id": 0, "thumbnail": "http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg"}, {"Genre_id": 1, "title": "Video 1", "Category_id": 1, "id": 1, "thumbnail": "http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg"}, {"Genre_id": 1, "title": "Video 2", "Category_id": 1, "id": 2, "thumbnail": "http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg"}, {"Genre_id": 1, "title": "Video 3", "Category_id": 1, "id": 3, "thumbnail": "http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg"}, {"Genre_id": 1, "title": "Video 4", "Category_id": 1, "id": 4, "thumbnail": "http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg"}, {"Genre_id": 1, "title": "Video 5", "Category_id": 1, "id": 5, "thumbnail": "http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg"}, {"Genre_id": 1, "title": "Video 6", "Category_id": 1, "id": 6, "thumbnail": "http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg"}, {"Genre_id": 1, "title": "Video 7", "Category_id": 1, "id": 7, "thumbnail": "http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg"}, {"Genre_id": 1, "title": "Video 8", "Category_id": 1, "id": 8, "thumbnail": "http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg"}, {"Genre_id": 1, "title": "Video 9", "Category_id": 1, "id": 9, "thumbnail": "http://img.ivi.ru/static/c8/0f69/c80f697da72360033f8a.1.jpg"}]
        assert len(res)==len(res_et)
        for i in res:
            assert i in res_et

    def test_promo_from_to(self):
        rv = self.app.get('/promo/?from=1&to=2')
        res=json.loads(rv.data)
        assert len(res)==2

    def test_promo_from_to100(self):
        rv = self.app.get('/promo/?from=5&to=100')
        res=json.loads(rv.data)
        assert len(res)==5


    def test_promo_from(self):
       rv = self.app.get('/promo/?from=1')
       res=json.loads(rv.data)
       assert len(res)==9

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
       assert len(res)==10



if __name__ == '__main__':
    unittest.main()