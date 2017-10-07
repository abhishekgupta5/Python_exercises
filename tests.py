import unittest
from notFlask import NotFlask


#Unittests
class TestNotFlask(unittest.TestCase):
    def setUp(self):
        self.app = NotFlask()

    def test_valid_route(self):
        @self.app.route('/')
        def index():
            return 'Testing Flask route'

        self.assertEqual(self.app.serve('/'), 'Testing Flask route')

    def test_invalid_route(self):
        with self.assertRaises(ValueError):
            self.app.serve('/random_url')


if __name__ == '__main__':
    unittest.main()
