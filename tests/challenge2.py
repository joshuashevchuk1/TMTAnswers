import unittest
import requests
import json

class Challenge2TestCase(unittest.TestCase):
    def test_challenge2(self):
        # Define the URL and query parameters
        url = 'http://127.0.0.1:8000/inventory/deactivate/'
        id = 5
        # Make the GET request
        response = requests.get(param={"pk":id},url)

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        print(json.dumps(response.json(), indent=4))