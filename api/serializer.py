from typing import Union
from decimal import Decimal
from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Product.

    Serializa todos los campos del modelo Product.
    
    Métodos:
        __init__(self, *args, **kwargs): Inicializa el serializador.
    """
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializerOrders(serializers.ModelSerializer):
    """
    Serializador para productos utilizados en consultas a pedidos.

    Serializa los campos 'reference', 'price_excl_tax', 'applicable_tax' y calcula 'amount' como la diferencia entre
    'applicable_tax' y 'price_excl_tax'.
    
    Campos:
        amount (SerializerMethodField): Diferencia entre 'applicable_tax' y 'price_excl_tax'.

    Métodos:
        get_amount(self, obj): Calcula la cantidad basada en la diferencia entre 'applicable_tax' y 'price_excl_tax'.
    """
    amount: serializers.SerializerMethodField = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['reference', 'price_excl_tax', 'applicable_tax', 'amount']

    def get_amount(self, obj: Product) -> Union[float, Decimal]:
        """
        Calcula la diferencia entre 'applicable_tax' y 'price_excl_tax'.

        Args:
            obj (Product): Instancia del modelo Product.

        Returns:
            Decimal: La diferencia entre 'applicable_tax' y 'price_excl_tax'.
        """
        return obj.applicable_tax - obj.price_excl_tax


class OrderCreateSerializer(serializers.ModelSerializer):
    """
    Serializador para la creación de pedidos.

    Incluye los campos 'id' y 'creation_date' del modelo Order.
    
    Métodos:
        __init__(self, *args, **kwargs): Inicializa el serializador.
    """
    class Meta:
        model = Order
        fields = ['id', 'creation_date']


class OrderReadSerializer(serializers.ModelSerializer):
    """
    Serializador para la lectura de pedidos.

    Serializa los campos del modelo Order, incluyendo los productos asociados y el total_amount calculado.
    
    Campos:
        products (ProductSerializerOrders): Productos asociados al pedido.
        total_amount (SerializerMethodField): Total de la cantidad calculada para todos los productos del pedido.
    
    Métodos:
        get_total_amount(self, obj): Calcula el total de la cantidad para todos los productos en el pedido.
    """
    products: serializers.SerializerMethodField = ProductSerializerOrders(many=True, read_only=True)
    total_amount: serializers.SerializerMethodField = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'creation_date', 'products', 'total_amount']

    def get_total_amount(self, obj: Order) -> Union[float, Decimal]:
        """
        Calcula el total de la cantidad para todos los productos en el pedido.

        Args:
            obj (Order): Instancia del modelo Order.

        Returns:
            Decimal: Suma de la diferencia entre 'applicable_tax' y 'price_excl_tax' para todos los productos en el pedido.
        """
        return sum(product.applicable_tax - product.price_excl_tax for product in obj.products.all())