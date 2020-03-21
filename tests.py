import unittest
import requests

BASE_URL = 'http://localhost:8000/'
ENDPOINT = 'capacity/'

class TestZipHrEndpoints(unittest.TestCase):

    # loads index
    def test_trivial(self):
        req = requests.get(BASE_URL)
        self.assertEqual(req.status_code, 400)

    # trivial test for capacity endpoint
    def test_capacity_no_args(self):
        req = requests.get(BASE_URL)
        self.assertEqual(req.status_code, 400)

    # test for capacity endpoint with letter in passengerNum param
    def test_for_capacity_endpoint_with_letter_in_passengerNum_param(self):
        request = BASE_URL + ENDPOINT + '?planeId=5&passengerNum=13z'
        req = requests.get(request)
        self.assertEqual(req.status_code, 401)

    def test_for_capacity_endpoint_with_letter_in_planeId_param(self):
        request = BASE_URL + ENDPOINT + '?planeId=z5&passengerNum=13'
        req = requests.get(request)
        self.assertEqual(req.status_code, 401)

    def test_for_missing_parameter_no_passengerNum(self):
        request = BASE_URL + ENDPOINT + '?planeId=5'
        req = requests.get(request)
        self.assertEqual(req.status_code, 401)

    def test_for_parameter_no_planeId(self):
        request = BASE_URL + ENDPOINT + '?passengerNum=599'
        req = requests.get(request)
        self.assertEqual(req.status_code, 401)

    # test for capacity with one arg correctly formatted of the form:
    # BASE_URL/capacity?id=[1-10]&num_passenger=1
    def test_single_plane_properly_formatted(self):
        request = BASE_URL + ENDPOINT +'?planeId=2&passengerNum=40'
        req = requests.get(request)
        self.assertEqual(req.status_code, 200)

if __name__ == "__main__":
    unittest.main()
