from django.db import models
from apps.product.models import Product
from apps.cart.models import Cart


class OrderItem(models.Model):
    quantity = models.IntegerField(verbose_name='quantidade')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='order_items')

    @property
    def price(self):
        return float(self.product.price) * self.quantity

    class Meta:
        verbose_name = 'Order_Item'
        verbose_name_plural = 'Order_Items'