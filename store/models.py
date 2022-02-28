from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.extfield()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField(default=1)
    last_update = models.DateTimeField(auto_now=True)
