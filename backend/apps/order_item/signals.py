from django.db.models.signals import pre_save
from .models import OrderItem
from apps.product.service import ProductService


def update_product_available_quantity_if_possible(sender, instance, **kwargs):
    ProductService.update_product_available_quantity(instance.product,
                                                     instance.quantity, )


pre_save.connect(
    update_product_available_quantity_if_possible, sender=OrderItem)
