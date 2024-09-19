from typing import List, Union
from django.urls import URLPattern, URLResolver
from django.contrib import admin
from django.urls import path, include

"""
Define las rutas URL para el proyecto Django.

Incluye las rutas para la interfaz de administración de Django y las rutas de la API.

Rutas:
    - path('admin/', admin.site.urls): Ruta para la interfaz de administración de Django.
    - path('api/v1/', include('api.urls')): Ruta base para las URL de la API, incluyendo las rutas definidas en el archivo 'api.urls'.
"""
urlpatterns: List[URLPattern] = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'))
]
