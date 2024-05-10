from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from interview.inventory.models import Inventory


class DeactivateOrderViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.order = Inventory.objects.create(name="Test Order", is_active=True)

    def test_deactivate_order(self):
        # Before deactivation
        self.assertTrue(self.order.is_active)

        # Deactivate the order
        response = self.client.post('/api/orders/deactivate/', {'pk': self.order.pk}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Reload the order from the database
        self.order.refresh_from_db()

        # After deactivation
        self.assertFalse(self.order.is_active)
