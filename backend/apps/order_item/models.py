from django.db import models
from apps.product.models import Product
from apps.cart.models import Cart

class OrderItem(models.Model):
    quantity = models.IntegerField(verbose_name='quantidade')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='preço')
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Oder_Item'
        verbose_name_plural = 'Order_Itens'
