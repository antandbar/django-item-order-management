from rest_framework import viewsets
from rest_framework.serializers import Serializer
from typing import Type
from .models import Product, Order
from .serializer import ProductSerializer, OrderCreateSerializer, OrderReadSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    Vista para las operaciones CRUD de productos.

    Esta vista proporciona las operaciones estándar para crear, leer, actualizar y eliminar productos
    utilizando el `ProductSerializer`. 

    Atributos:
        queryset (QuerySet): Conjunto de consultas que representa todos los productos disponibles.
        serializer_class (Serializer): Serializador utilizado para convertir instancias de `Product` en 
        representaciones JSON y viceversa.
    """
    queryset=Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    Vista para las operaciones CRUD de pedidos.

    Esta vista proporciona las operaciones estándar para crear, leer, actualizar y eliminar pedidos.
    Utiliza diferentes serializadores según la acción realizada en la vista.

    Atributos:
        queryset (QuerySet): Conjunto de consultas que representa todos los pedidos disponibles.

    Métodos:
        get_serializer_class(self): Devuelve el serializador adecuado según la acción realizada.
            - `list`, `retrieve`: Utiliza `OrderReadSerializer`.
            - Otras acciones (por ejemplo, `create`): Utiliza `OrderCreateSerializer`.
    """
    queryset=Order.objects.all()
    def get_serializer_class(self) -> Type[Serializer]:
        """
        Devuelve el serializador adecuado basado en la acción de la vista.

        Este método selecciona el serializador que se usará para la acción solicitada en la vista:
        - Para las acciones 'list' y 'retrieve', devuelve `OrderReadSerializer`.
        - Para otras acciones (como `create` o `update`), devuelve `OrderCreateSerializer`.

        Returns:
            Serializer: El serializador correspondiente según la acción realizada.
        """
        if self.action in ['list', 'retrieve']:  
            return OrderReadSerializer
        return OrderCreateSerializer  
