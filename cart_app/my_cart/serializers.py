from django.contrib.auth.models import User
from rest_framework import serializers

from my_cart.enumeration import ProductStatusEnum
from my_cart.models import Products, Cart


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = "__all__"

    def get_status(self, instance):
        status = instance.status
        if status == 1:
            return ProductStatusEnum.AVAILABLE.status_name()
        else:
            return ProductStatusEnum.OUT_OF_STOCK.status_name()


class CartCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartListSerializer(serializers.ModelSerializer):
    products = ProductSerializer()

    class Meta:
        model = Cart
        fields = "__all__"
