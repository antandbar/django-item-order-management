from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..models import Product, Order

class ProductAPITest(APITestCase):

    def setUp(self):
        """Configurar la orden para los tests"""
        self.order = Order.objects.create()

    def test_create_product(self):
        """Prueba que se pueda crear un producto a través de la API"""
        url = reverse('product-list')  # Usa el router de DRF para definir el endpoint
        data = {
            'reference': 'ref002',
            'name': 'Macbook',
            'description': 'Macbook Pro 16',
            'price_excl_tax': 2000.00,
            'applicable_tax': 2400.00,
            'order': self.order.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Macbook')

    def test_unique_reference_api(self):
        """Prueba que no se pueda crear un producto con referencia duplicada vía API"""
        Product.objects.create(
            reference='ref003',
            name='iPhone',
            description='iPhone 14',
            price_excl_tax=1000.00,
            applicable_tax=1200.00,
            order=self.order
        )
        url = reverse('product-list')
        data = {
            'reference': 'ref003',  # Mismo reference
            'name': 'iPhone 15',
            'description': 'iPhone 15',
            'price_excl_tax': 1100.00,
            'applicable_tax': 1300.00,
            'order': self.order.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Espera un error por la referencia duplicada
