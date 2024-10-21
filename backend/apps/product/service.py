from apps.shared.base_service import BaseService
from apps.shared.custom_api_exception import CustomAPIException
from .repository import ProductRepository


class ProductService(BaseService):

    @staticmethod
    def list_all_instances():
        try:
            return ProductRepository.get_all_instances()
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(detail=str(e), status_code=500)

    @staticmethod
    def retrieve_instance(instance_id):
        try:
            return ProductRepository.get_instance_by_id(instance_id)
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(detail=str(e), status_code=500)

    @staticmethod
    def create_instance(validated_data):
        try:
            return ProductRepository.create_instance(validated_data)
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail='Failed to create product: ' + str(e), status_code=500)

    @staticmethod
    def update_instance_and_partial_update(instance_id, validated_data):
        try:
            return ProductRepository.update_instance(instance_id,
                                                     validated_data)
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail='Failed to update product: ' + str(e), status_code=500)

    @staticmethod
    def destroy_instance(instance_id):
        try:
            ProductRepository.delete_instance(instance_id)
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail='Failed to delete product: ' + str(e), status_code=500)

    @staticmethod
    def update_product_available_quantity(product, quantity):
        new_available_quantity = product.available_quantity - quantity
        if new_available_quantity < 0:
            raise CustomAPIException(
                detail='Not enough product available', status_code=400)
        data = {
            'available_quantity': product.available_quantity - quantity
        }
        ProductRepository.update_instance(product.id, data)
