from django.db.models.signals import post_save
from .models import Product
from apps.order_item.service import OrderItemService


def check_if_there_is_enough_product(sender, instance, created, **kwargs):
    if not created:
        OrderItemService.check_if_there_is_enough_product_and_update_if_needed_order_items(instance)  # noqa (E501)


post_save.connect(check_if_there_is_enough_product, sender=Product)
