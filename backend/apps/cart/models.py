from django.db import models
from django.contrib.auth import get_user_model
from .managers import ManagerCart

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    objects = ManagerCart()

    def __str__(self):
        return 'carrinho do usuário: ' + self.user.name
