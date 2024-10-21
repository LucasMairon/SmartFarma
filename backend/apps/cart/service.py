from apps.shared.base_service import BaseService
from apps.shared.custom_api_exception import CustomAPIException
from .repository import CartRepository


class CartService(BaseService):

    @staticmethod
    def list_all_instances():
        try:
            return CartRepository.get_all_instances()
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(detail=str(e), status_code=500)

    @staticmethod
    def create_instance(validated_data):
        try:
            return CartRepository.create_instance(validated_data)
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail="Failed to create user: " + str(e), status_code=500)

    @staticmethod
    def retrieve_instance(instance_id):
        try:
            return CartRepository.get_instance_by_id(instance_id)
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(detail=str(e), status_code=500)

    @staticmethod
    def update_instance_and_partial_update(instance_id, validated_data):
        try:
            return CartRepository.update_instance(instance_id, validated_data)
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail="Failed to update user: " + str(e), status_code=500)

    @staticmethod
    def destroy_instance(instance_id):
        try:
            CartRepository.delete_instance(instance_id)
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail="Failed to delete user: " + str(e), status_code=500)

    @staticmethod
    def get_or_create(user_id):
        try:
            queryset_carrinho = CartRepository.get_all_instances_for_user(
                user_id)
            if queryset_carrinho.exists():
                return queryset_carrinho.first()
            return CartRepository.create_instance(
                {'user_id': user_id, 'is_active': True})
        except CustomAPIException:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail="Failed to get or create user: " + str(e),
                status_code=500)
