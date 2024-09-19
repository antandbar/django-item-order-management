from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..models import Product, Order

class ProductAPITest(APITestCase):
    """
    Pruebas de la API para el modelo Product.

    Esta clase contiene pruebas que verifican la funcionalidad de la API para crear productos y 
    garantizar que las restricciones, como la unicidad de la referencia del producto, se apliquen correctamente.

    Métodos:
        setUp(self): Configura un pedido para usar en las pruebas.
        test_create_product(self): Verifica que se pueda crear un producto a través de la API.
        test_unique_reference_api(self): Verifica que no se pueda crear un producto con una referencia duplicada a través de la API.
    """

    def setUp(self):
        """
        Configura el entorno para las pruebas creando una instancia de pedido.

        Esta instancia de pedido se utiliza para asociar productos en las pruebas.
        """
        self.order = Order.objects.create()

    def test_create_product(self):
        """
        Verifica que se pueda crear un producto a través de la API.

        Envía una solicitud POST para crear un nuevo producto y verifica que la respuesta tenga un código de estado 201 
        (creado), que se haya creado un producto en la base de datos y que el nombre del producto sea el esperado.
        """
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
        """
        Verifica que no se pueda crear un producto con una referencia duplicada a través de la API.

        Primero se crea un producto con una referencia específica. Luego, se intenta crear otro producto con la misma 
        referencia y se verifica que la respuesta tenga un código de estado 400 (solicitud incorrecta) debido a la 
        restricción de unicidad en la referencia.
        """
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
