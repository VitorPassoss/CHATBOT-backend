from django.db import models
from apps.products.models.supplier import Supplier




class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(
        max_digits=21, decimal_places=3, blank=True, null=True
    )
    supplie_fk = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True)
    weight = models.DecimalField(
        max_digits=21, decimal_places=3, blank=True, null=True
    )
