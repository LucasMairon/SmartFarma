from apps.shared.base_repositoy import BaseRepository
from .models import Address
from apps.shared.custom_api_exception import CustomAPIException


class AddressRepository(BaseRepository):

    @staticmethod
    def create_instance(validated_data):
        return Address.objects.create(**validated_data)

    @staticmethod
    def get_all_instances():
        return Address.objects.all()

    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            return Address.objects.get(id=instance_id)
        except Address.ObjectDoesNotExist:
            raise CustomAPIException(
                detail='address not found.', status_code=404)

    @staticmethod
    def update_instance(instance_id, validated_data):
        try:
            address = Address.objects.get(id=instance_id)
            for attr, value in validated_data.items():
                setattr(address, attr, value)
            address.save()
            return address
        except Address.ObjectDoesNotExist:
            raise CustomAPIException("address not found",  status_code=404)

    @staticmethod
    def delete_instance(instance_id):
        try:
            address = Address.objects.get(id=instance_id)
            address.delete()
        except Address.ObjectDoesNotExist:
            raise CustomAPIException("address not found",  status_code=404)

    @staticmethod
    def get_all_instances_for_user(user_id):
        return Address.objects.filter(user=user_id)
