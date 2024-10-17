from django.db import models

from django.contrib.auth import get_user_model
from .validators import (
    street_regex_validator,
    city_regex_validator,
    state_regex_validator,
    number_regex_validator,
    neighborhood_regex_validator,
    complement_regex_validator,
    reference_point_regex_validator,
    zip_code_regex_validator
)


User = get_user_model()


class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='addresses')
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
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street}, {self.number} - {self.neighborhood}, {self.city} - {self.state}"
