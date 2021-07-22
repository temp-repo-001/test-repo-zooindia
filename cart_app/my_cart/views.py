from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny

from my_cart.forms import NewUserForm
from my_cart.models import Products, Cart
from my_cart.serializers import (
    UserCreateSerializer,
    ProductSerializer,
    CartCreateUpdateSerializer,
    CartListSerializer,
    ProductListSerializer,
)


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("some_html")
    else:
        form = NewUserForm()
    return render(request, "register.html", {form: form})


def product_list(request):
    products = Products.objects.all()
    return render(request, "products.html", {"products": products})


class UserCreateAPIView(ListCreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Products.objects.all()
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductSerializer
        return ProductListSerializer


class ProductUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return ProductSerializer
        return ProductListSerializer


class CartCreateListAPIView(ListCreateAPIView):
    queryset = Cart.objects.all()
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CartCreateUpdateSerializer
        return CartListSerializer


class CartUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return CartCreateUpdateSerializer
        return CartListSerializer
