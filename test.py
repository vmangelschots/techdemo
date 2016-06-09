import unittest
from hello import app
class Testapp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
 
    def test_entry(self):
        rv = self.app.get('/')
        self.assertEqual(rv.data,"Hello, Belgie!")
 
if __name__ == '__main__':
    unittest.main()