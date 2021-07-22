from django.contrib import admin

# Register your models here.
from my_cart.models import Products, Cart

admin.site.register(Products)
admin.site.register(Cart)
