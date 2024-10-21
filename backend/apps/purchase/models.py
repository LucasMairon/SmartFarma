from django.db import models
from apps.users.models import CustomUser
from apps.cart.models import Cart
from .validators import (
    city_regex_validator,
    street_regex_validator,
    state_regex_validator,
    number_regex_validator,
    neighborhood_regex_validator,
    complement_regex_validator,
    reference_point_regex_validator,
    zip_code_regex_validator,
)

STATUS_CHOICES = {
    'A': 'Em Aberto',
    'F': 'Fechada',
}


class Purchase(models.Model):
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    street = models.CharField(
        max_length=100,
        validators=[street_regex_validator]
    )
    city = models.CharField(max_length=50, validators=[city_regex_validator])
    state = models.CharField(max_length=50, validators=[state_regex_validator])
    number = models.CharField(
        max_length=50,
        validators=[number_regex_validator]
    )
    neighborhood = models.CharField(
        max_length=50,
        validators=[neighborhood_regex_validator]
    )
    complement = models.CharField(
        max_length=50,
        validators=[complement_regex_validator]
    )
    reference_point = models.CharField(
        max_length=50,
        validators=[reference_point_regex_validator]
    )
    zip_code = models.CharField(
        max_length=50,
        validators=[zip_code_regex_validator]
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'purchase'
        verbose_name_plural = 'purchases'
