import unittest
import requests
import json

class Challenge3TestCase(unittest.TestCase):
    def test_orders_between_dates(self):
        # Define the URL and query parameters
        url = 'http://127.0.0.1:8000/inventory/created-after/2024-05-01/'
        # Make the GET request
        response = requests.get(url)

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        print(json.dumps(response.json(), indent=4))

