from apps.shared.base_repositoy import BaseRepository
from .models import OrderItem
from apps.shared.custom_api_exception import CustomAPIException
from apps.product.api.serializers import ProductSerializer


class OrderItemRepository(BaseRepository):

    @staticmethod
    def create_instance(validated_data):
        return OrderItem.objects.create(**validated_data)

    @staticmethod
    def get_all_instances():
        order_itens = OrderItem.objects.all()
        for order_item in order_itens:
            product = ProductSerializer(order_item.product)
            order_item.product = product
            order_item.save()
        return OrderItem.objects.all()

    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            order_item = OrderItem.objects.get(id=instance_id)
            order_item.product = ProductSerializer(order_item.product)
            return order_item
        except OrderItem.DoesNotExist:
            raise CustomAPIException(
                detail='order item not found', status_code=404
            )

    @staticmethod
    def update_instance(instance_id, validated_data):
        try:
            order_item = OrderItem.objects.get(id=instance_id)
            for attr, value in validated_data.items():
                setattr(order_item, attr, value)
            order_item.save()
            return order_item
        except OrderItem.DoesNotExist:
            raise CustomAPIException('order item not found', status_code=404)

    @staticmethod
    def delete_instance(instance_id):
        try:
            order_item = OrderItem.objects.get(id=instance_id)
            order_item.delete()
        except OrderItem.DoesNotExist:
            raise CustomAPIException('order item not found', status_code=404)
