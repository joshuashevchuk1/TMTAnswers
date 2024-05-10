import unittest
import requests
import json

class OrderBetweenDatesTestCase(unittest.TestCase):
    def test_orders_between_dates(self):
        # Define the URL and query parameters
        url = 'http://localhost:8000/orders/orders-between-dates/'
        start_date = '2024-05-01'
        embargo_date = '2024-06-09'

        # Make the GET request
        response = requests.get(url, params={'start_date': start_date, 'embargo_date': embargo_date})

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        print(json.dumps(response.json(), indent=4))

