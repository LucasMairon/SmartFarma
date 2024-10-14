from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)
    complement = models.CharField(max_length=50)
    reference_point = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street}, {self.number} - {self.neighborhood}, {self.city} - {self.state}"
