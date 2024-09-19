from django.urls import path, include
from rest_framework import routers
from api import views

"""
Configuración de URLs para la API de productos y pedidos.

Este archivo define las rutas para la API utilizando el enrutador de Django REST Framework. 
Registra las vistas `ProductViewSet` y `OrderViewSet` para manejar las solicitudes relacionadas con 
productos y pedidos, respectivamente.

El enrutador crea automáticamente las rutas para las operaciones CRUD básicas, como listar, 
detallar, crear, actualizar y eliminar instancias de productos y pedidos.

Rutas:
    - 'products': Registra las rutas para las operaciones CRUD de productos.
    - 'orders': Registra las rutas para las operaciones CRUD de pedidos.
"""
router: routers.DefaultRouter = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]
