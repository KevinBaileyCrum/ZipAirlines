import unittest
import requests

BASE_URL = 'http://localhost:8000'

class TestZipHrEndpoints(unittest.TestCase):

    def test_trivial(self):
        req = requests.get(BASE_URL)
        print(req.status_code)
        # self.assertEqual(req.status_code, 200)

if __name__ == "__main__":
    unittest.main()
