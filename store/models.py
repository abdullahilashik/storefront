from django.db import models

class Product(models.Model):
    # sku = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.extfield()
    price  = models.DecimalField(max_digits=6 ,decimal_places=2)
    inventory = models.IntegerField(default=1)
    last_update = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)