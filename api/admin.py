from django.contrib import admin
from .models import Product, Order

"""
Registro en administración Django.

Este archivo registra los modelos `Order` y `Product` en el panel de administración de Django.
Esto permite gestionar estos modelos a través de la interfaz de administración proporcionada por Django.
"""

admin.site.register(Order)
admin.site.register(Product)
