__author__ = 'eross'

import api
import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_promo(self):
        rv = self.app.get('/promo')
        assert 'No entries here so far' in rv.data