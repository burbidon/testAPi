__author__ = 'eross'

import api
import unittest

class APITestCase(unittest.TestCase):

    def setUp(self):
         self.app = api.app.test_client()

    def tearDown(self):
        pass

    def test_promo(self):
        rv = self.app.get('/promo')
        assert 'No entries here so far' in rv.data


if __name__ == '__main__':
    unittest.main()