from django.db import models
from apps.products.models.supplier import Supplier
from apps.products.models.product import Product


class Stock(models.Model):
    supplie_fk = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    product_fk = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    
   