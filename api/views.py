from rest_framework import viewsets
from .models import Product, Order
from .serializer import ProductSerializer, OrderCreateSerializer, OrderReadSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  
            return OrderReadSerializer
        return OrderCreateSerializer  
