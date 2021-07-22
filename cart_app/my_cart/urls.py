from django.urls import path

from my_cart import views

urlpatterns = [
    path("", views.register, name="register"),
    path("products-html/", views.product_list, name="products"),
    path("create-user/", views.UserCreateAPIView.as_view(), name="user-create"),
    path("products/", views.ProductListCreateAPIView.as_view(), name="product-create"),
    path(
        "products/<int:pk>/", views.ProductUpdateView.as_view(), name="product-update"
    ),
    path("cart/", views.CartCreateListAPIView.as_view(), name="cart-create"),
    path("cart/<int:pk>/", views.CartUpdateAPIView.as_view(), name="cart-update"),
]
