__author__ = 'eross'

import api
import unittest
import json

class APITestCase(unittest.TestCase):

    def setUp(self):
         self.app = api.app.test_client()

    def tearDown(self):
        pass

    def test_promo(self):
        rv = self.app.get('/promo/')
        res=json.loads(rv.data)
        res_et=[{'Genre_id': 1, 'Category_id': 1, 'id': 0, 'title': 'Video 0'}, {'Genre_id': 1, 'Category_id': 1, 'id': 1, 'title': 'Video 1'}, {'Genre_id': 1, 'Category_id': 1, 'id': 2, 'title': 'Video 2'}, {'Genre_id': 1, 'Category_id': 1, 'id': 3, 'title': 'Video 3'}, {'Genre_id': 1, 'Category_id': 1, 'id': 4, 'title': 'Video 4'}, {'Genre_id': 1, 'Category_id': 1, 'id': 5, 'title': 'Video 5'}, {'Genre_id': 1, 'Category_id': 1, 'id': 6, 'title': 'Video 6'}, {'Genre_id': 1, 'Category_id': 1, 'id': 7, 'title': 'Video 7'}, {'Genre_id': 1, 'Category_id': 1, 'id': 8, 'title': 'Video 8'}, {'Genre_id': 1, 'Category_id': 1, 'id': 9, 'title': 'Video 9'}]
        assert res==res_et

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

    def test_promo_to(self):
       rv = self.app.get('/promo/?from=10&to=1')
       assert 'error' in rv.data


if __name__ == '__main__':
    unittest.main()