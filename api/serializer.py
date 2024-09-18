from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializerOrders(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['reference', 'price_excl_tax', 'applicable_tax', 'amount']

    def get_amount(self, obj):
        return obj.applicable_tax - obj.price_excl_tax

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'creation_date']

class OrderReadSerializer(serializers.ModelSerializer):
    products = ProductSerializerOrders(many=True, read_only=True)
    total_amount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'creation_date', 'products', 'total_amount']

    def get_total_amount(self, obj):
        return sum(product.applicable_tax - product.price_excl_tax for product in obj.products.all())