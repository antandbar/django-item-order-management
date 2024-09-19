from django.test import TestCase
from ..models import Product, Order
from django.db.utils import IntegrityError

class ProductModelTest(TestCase):

    def setUp(self):
        """Crear datos iniciales para las pruebas"""
        self.order = Order.objects.create()
        self.product1 = Product.objects.create(
            reference='ref001',
            name='Product 1',
            description='Description for product 1',
            price_excl_tax=100.00,
            applicable_tax=120.00,
            order=self.order
        )

    def test_product_creation(self):
        """Prueba que se pueda crear un producto correctamente"""
        product_count = Product.objects.count()
        self.assertEqual(product_count, 1)

    def test_unique_reference(self):
        """Prueba que no se puedan crear productos con la misma referencia"""
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                reference='ref001',  # Misma referencia que product1
                name='Product 2',
                description='Description for product 2',
                price_excl_tax=150.00,
                applicable_tax=180.00,
                order=self.order
            )

    def test_amount_calculation(self):
        """Prueba que la cantidad se calcule correctamente"""
        self.assertEqual(self.product1.applicable_tax - self.product1.price_excl_tax, 20.00)