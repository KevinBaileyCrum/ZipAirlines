import unittest
import requests

BASE_URL = 'http://localhost:8000/'
ENDPOINT = 'capacity/'

class TestZipHrEndpoints(unittest.TestCase):

    ###################################################################
    # trivial test cases
    ###################################################################

    # loads index
    def test_trivial(self):
        req = requests.get(BASE_URL)
        self.assertEqual(req.status_code, 400)

    # trivial test for capacity endpoint
    def test_capacity_no_args(self):
        req = requests.get(BASE_URL)
        self.assertEqual(req.status_code, 400)

    ###################################################################
    # poorly formed URL paramters
    ###################################################################

    # test for capacity endpoint with letter in passengerNum param
    def test_for_capacity_endpoint_with_letter_in_passengerNum_param(self):
        request = BASE_URL + ENDPOINT + '?planeId=5&passengerNum=13z'
        req = requests.get(request)
        self.assertEqual(req.status_code, 401)

    def test_for_capacity_endpoint_with_letter_in_planeId_param(self):
        request = BASE_URL + ENDPOINT + '?planeId=z5&passengerNum=13'
        req = requests.get(request)
        self.assertEqual(req.status_code, 401)

    def test_for_capacity_endpoint_with_letter_in_middle_of_good_queries(self):
        request = BASE_URL + ENDPOINT + '?planeId=3&passengerNum=1&planeId=1&passengerNum=5&planeId=4&passengerNum=l9'
        req = requests.get(request)
        self.assertEqual(req.status_code, 401)
        request = BASE_URL + ENDPOINT + '?planeId=3&passengerNum=1&planeId=x1&passengerNum=5&planeId=4&passengerNum=9'
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

    def test_for_capacity_endpoint_with_missing_param_in_middle_of_good_queries(self):
        request = BASE_URL + ENDPOINT + '?planeId=3&passengerNum=1&planeId=1&planeId=4&passengerNum=9'
        req = requests.get(request)
        self.assertEqual(req.status_code, 401)
        request = BASE_URL + ENDPOINT + '?planeId=3&passengerNum=1&&planeId=4'
        req = requests.get(request)
        self.assertEqual(req.status_code, 401)

    def test_for_division_by_zero(self):
        request = BASE_URL + ENDPOINT + '?planeId=1&passengerNum=0'
        req = requests.get(request)
        self.assertEqual(req.status_code, 401)

    ###################################################################
    # successful queries
    ###################################################################
    # test for capacity with one arg correctly formatted of the form:
    # BASE_URL/capacity?id=[1-10]&num_passenger=1
    def test_single_plane_properly_formatted(self):
        request = BASE_URL + ENDPOINT +'?planeId=2&passengerNum=40'
        req = requests.get(request)
        self.assertEqual(req.status_code, 200)

    def test_ten_plane_properly_formatted(self):
        request = BASE_URL + ENDPOINT +'?planeId=1&passengerNum=250&planeId=2&passengerNum=250&planeId=3&passengerNum=250&planeId=4&passengerNum=250&planeId=5&passengerNum=250&planeId=6&passengerNum=250&planeId=7&passengerNum=250&planeId=8&passengerNum=250&planeId=9&passengerNum=250&planeId=10&passengerNum=250'
        req = requests.get(request)
        self.assertEqual(req.status_code, 200)

    # for testing math id expect the same plane id with increasing capacity to drop in minutes to run
    def test_same_planeId_increasing_capacity_for_monotonicity(self):
        request = BASE_URL + ENDPOINT +'?planeId=3&passengerNum=10&planeId=3&passengerNum=100&planeId=3&passengerNum=1000'
        req = requests.get(request)
        data = req.json()
        i = 0
        j = 1
        while j < len(data):
            self.assertTrue(data[i]['minutesOfFlight'] > data[j]['minutesOfFlight'])
            i += 1
            j += 1


    def trivial_math_test(self):
        expPlaneId = 1
        expPassengernum = 1
        expLitersPerMinute = 0.002
        expMinutesOfFlight = 100000.0
        request = BASE_URL + ENDPOINT +'?planeId=1&passengerNum=1'
        req = requests.get(request)
        data = req.json()
        self.assertEqual(data[0]['planeId'], 1)
        self.assertEqual(data[0]['passengerNum'], 1)
        self.assertEqual(data[0]['litersPerMinute'], 1)
        self.assertEqual(data[0]['minutesOfFlight'], 1)



if __name__ == "__main__":
    unittest.main()
    ###################################################################
    # successful queries
    ###################################################################
    # test for capacity with one arg correctly formatted of the form:
    # BASE_URL/capacity?id=[1-10]&num_passenger=1
    def test_single_plane_properly_formatted(self):
        request = BASE_URL + ENDPOINT +'?planeId=2&passengerNum=40'
        req = requests.get(request)
        self.assertEqual(req.status_code, 200)

