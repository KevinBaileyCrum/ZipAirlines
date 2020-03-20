import unittest
import requests

BASE_URL = 'http://localhost:8000'

class TestZipHrEndpoints(unittest.TestCase):

    # loads index
    def test_trivial(self):
        req = requests.get(BASE_URL)
        self.assertEqual(req.status_code, 200)

    # trivial test for capacity endpoint
    def test_capacity_no_args(self):
        req = requests.get(BASE_URL)
        self.assertEqual(req.status_code, 200)

if __name__ == "__main__":
    unittest.main()
