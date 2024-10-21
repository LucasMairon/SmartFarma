from apps.shared.base_service import BaseService
from apps.shared.custom_api_exception import CustomAPIException
from .repository import OrderItemRepository
from apps.product.service import ProductService


class OrderItemService(BaseService):

    @staticmethod
    def list_all_instances():
        try:
            return OrderItemRepository.get_all_instances()
        except CustomAPIException as e:
            raise CustomAPIException(detail=str(e), status_code=500)

    @staticmethod
    def create_instance(validated_data):
        try:
            return OrderItemRepository.create_instance(validated_data)
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail='Failed to create order item: ' + str(e),
                status_code=500
            )

    @staticmethod
    def retrieve_instance(instance_id):
        try:
            return OrderItemRepository.get_instance_by_id(instance_id)
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(detail=str(e), status_code=500)

    @staticmethod
    def update_instance_and_partial_update(instance_id, validated_data):
        try:
            OrderItemRepository.update_instance(instance_id, validated_data)
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail='Failed to update order item: ' + str(e),
                status_code=500
            )

    @staticmethod
    def destroy_instance(instance_id):
        try:
            OrderItemRepository.delete_instance(instance_id)
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail='Failed to delete order item: ' + str(e),
                status_code=500
            )

    @staticmethod
    def check_if_there_is_enough_product(instance):
        if instance.quantity > instance.product.available_quantity:
            raise CustomAPIException(
                detail='There is not enough product in stock', status_code=400
            )

    @staticmethod
    def update_product_available_quantity(instance):
        ProductService.update_product_available_quantity(
            instance.product, instance.quantity)

    @staticmethod
    def update_order_quantity(instance):
        data = {
            '.quantity': instance.quantity - instance.product.quantity
        }
        OrderItemRepository.update_instance(instance.id, data)
