from apps.shared.base_repositoy import BaseRepository
from .models import Cart
from apps.shared.custom_api_exception import CustomAPIException


class CartRepository(BaseRepository):

    @staticmethod
    def create_instance(validated_data):
        return Cart.objects.create(**validated_data)

    @staticmethod
    def get_all_instances():
        return Cart.objects.all()

    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            return Cart.objects.get(id=instance_id)
        except Cart.ObjectDoesNotExist:
            raise CustomAPIException(
                detail='Cart not found.', status_code=404)

    @staticmethod
    def update_instance(instance_id, validated_data):
        try:
            cart = Cart.objects.get(id=instance_id)
            for attr, value in validated_data.items():
                setattr(cart, attr, value)
            cart.save()
            return cart
        except Cart.ObjectDoesNotExist:
            raise CustomAPIException("Cart not found",  status_code=404)

    @staticmethod
    def delete_instance(instance_id):
        try:
            cart = Cart.objects.get(id=instance_id)
            cart.delete()
        except Cart.ObjectDoesNotExist:
            raise CustomAPIException("Cart not found",  status_code=404)

    @staticmethod
    def get_all_instances_for_user(user_id):
        return Cart.objects.filter(user_id=user_id, is_active=True)
