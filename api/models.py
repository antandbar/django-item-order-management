from django.db import models


class Order(models.Model):
    """
    Modelo que representa un pedido.

    Atributos:
        creation_date (DateTimeField): Fecha y hora en la que se crea el pedido, se asigna automáticamente.
    
    Métodos:
    __str__(): Devuelve una representación en cadena del pedido, incluyendo el ID y la fecha de creación.
    """
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        Representación en cadena del objeto Order.

        Returns:
            str: Una cadena que muestra el ID del pedido y la fecha de creación.
        """
        return f"Order {self.id} - {self.creation_date}"


class Product(models.Model):
    """
    Modelo que representa un producto asociado a un pedido.

    Atributos:
        reference (CharField): Referencia única del producto.
        name (CharField): Nombre del producto.
        description (TextField): Descripción del producto.
        price_excl_tax (DecimalField): Precio del producto sin impuestos.
        applicable_tax (DecimalField): Importe del impuesto aplicable al producto.
        creation_date (DateTimeField): Fecha y hora en la que se crea el producto, se asigna automáticamente.
        order (ForeignKey): Relación de clave externa con el modelo Order, indicando a qué pedido pertenece el producto. Puede ser nulo o estar en blanco.
    
    Métodos:
        __str__(): Devuelve una representación en cadena del producto, mostrando su nombre.
    """
    reference = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_excl_tax = models.DecimalField(max_digits=10, decimal_places=2)
    applicable_tax = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, related_name='products', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        """
        Representación en cadena del objeto Product.

        Returns:
            str: Una cadena que muestra el nombre del producto.
        """
        return self.name