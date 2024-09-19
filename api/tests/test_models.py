from django.test import TestCase
from ..models import Product, Order
from django.db.utils import IntegrityError

class ProductModelTest(TestCase):
    """
    Pruebas del modelo Product.

    Esta clase contiene pruebas que verifican la correcta creación de pedidos y productos, la unicidad de la referencia del producto, 
    y el cálculo correcto de la cantidad.

    Métodos:
        setUp(self): Configura el entorno para las pruebas creando una instancia de pedido y un producto.
        test_product_creation(self): Verifica que se pueda crear un producto correctamente.
        test_unique_reference(self): Verifica que no se puedan crear productos con la misma referencia.
        test_amount_calculation(self): Verifica que la cantidad se calcule correctamente.
    """

    def setUp(self):
        """
        Configura el entorno para las pruebas creando una instancia de pedidos y un producto.

        Esta instancia de pedidos se usa para asociar productos en las pruebas. Además, se crea un producto con una referencia 
        específica para probar la funcionalidad del modelo.
        """
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
        """
        Verifica que se pueda crear un producto correctamente.

        Cuenta el número de productos en la base de datos y asegura que sea 1, confirmando que el producto se creó 
        correctamente.
        """
        product_count = Product.objects.count()
        self.assertEqual(product_count, 1)

    def test_unique_reference(self):
        """
        Verifica que no se puedan crear productos con la misma referencia.

        Intenta crear un segundo producto con la misma referencia que el primero y asegura que se lance una excepción 
        `IntegrityError`, confirmando que la restricción de unicidad en la referencia está funcionando.
        """
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
        """
        Verifica que la cantidad se calcule correctamente.

        Calcula la diferencia entre 'applicable_tax' y 'price_excl_tax' para el producto creado y asegura que sea 20.00, 
        verificando que el cálculo es correcto.
        """
        self.assertEqual(self.product1.applicable_tax - self.product1.price_excl_tax, 20.00)

    