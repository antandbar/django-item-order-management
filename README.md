# Proyecto Django - API de Productos y Pedidos

## Descripción

Este proyecto es una API RESTful construida con Django y Django REST Framework (DRF) para gestionar productos y pedidos. La API permite realizar operaciones CRUD sobre productos y pedidos, y proporciona funcionalidades para calcular impuestos y totalizar montos asociados a los productos.

## Características

- **Gestión de Productos**: Crear, leer, actualizar y eliminar productos.
- **Gestión de Pedidos**: Crear, leer, actualizar y eliminar pedidos.
- **Cálculo de Montos**: Calcula la diferencia entre el impuesto aplicable y el precio sin impuestos de los productos.
- **Endpoints de API**:
  - `/api/v1/products/` - CRUD para productos.
  - `/api/v1/orders/` - CRUD para pedidos.

## Tecnologías

- **Django**: Framework web para desarrollo rápido.
- **Django REST Framework**: Toolkit para construir APIs web en Django.
- **PostgreSQL**: Base de datos utilizada.

## Instalación

Sigue estos pasos para instalar y configurar el proyecto:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git

2. **Navega al directorio del proyecto:**

    cd tu_repositorio

3. **Construye y levanta los contenedores:**

    docker-compose up --build

4. **Realiza las migraciones de la base de datos:**

    docker compose run web python manage.py migrate

5. **Crea un superusuario para acceder al panel de administración:**

    docker-compose run web python manage.py createsuperuser

6. **Accede a la aplicación en tu navegador:**

    La aplicación estará disponible en http://0.0.0.0:8000/

## Endpoints de API

    . Productos
        . GET /api/v1/products/: Lista todos los productos.
        . POST /api/v1/products/: Crea un nuevo producto.
        . GET /api/v1/products/{id}/: Obtiene detalles de un producto específico.
        . PUT /api/v1/products/{id}/: Actualiza un producto específico.
        . DELETE /api/v1/products/{id}/: Elimina un producto específico.

    . Pedidos
        . GET /api/v1/orders/: Lista todos los pedidos.
        . POST /api/v1/orders/: Crea un nuevo pedido.
        . GET /api/v1/orders/{id}/: Obtiene detalles de un pedido específico.
        . DELETE /api/v1/orders/{id}/: Elimina un pedido específico.

## Pruebas

    docker-compose run web python manage.py test

## Pg_admin

    http://localhost/

## Contacto

    . Autor: Antonio Andreu Barreiro
    . Repositorio: https://github.com/antandbar/django-item-order-management

