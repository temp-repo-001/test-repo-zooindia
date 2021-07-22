from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from my_cart.models import Cart


class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        max_length=256, help_text="Required! Add only valid email ids"
    )
    first_name = forms.CharField(
        max_length=256, required=False, help_text="Optional : First Name"
    )
    last_name = forms.CharField(
        max_length=256, required=False, help_text="Optional : Last Name"
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ["products", "units"]
