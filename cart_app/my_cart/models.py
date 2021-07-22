from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.PositiveIntegerField(default=0, null=True, blank=True)
    image = models.ImageField(upload_to="upload/", null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    units = models.PositiveIntegerField(default=1)
    order_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.products
