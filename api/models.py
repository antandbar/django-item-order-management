from django.db import models

class Order(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.creation_date}"

class Product(models.Model):
    reference = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_excl_tax = models.DecimalField(max_digits=10, decimal_places=2)
    applicable_tax = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, related_name='products', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name