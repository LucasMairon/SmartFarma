from django.db import transaction
from apps.shared.base_service import BaseService
from apps.shared.custom_api_exception import CustomAPIException
from .repository import UserRepository


class UserService(BaseService):

    @staticmethod
    def list_all_instances():
        try:
            return UserRepository.get_all_instances()
        except CustomAPIException as e:
            raise
        except Exception as e:
            raise CustomAPIException(detail=str(e), status_code=500)

    @staticmethod
    def create_instance(validated_data):
        try:
            with transaction.atomic():
                address_data = validated_data.pop("address")
                user = UserRepository.create_instance(validated_data)
                address_data['user'] = user.id
                AddressService.create_instance(address_data)
                return user
        except CustomAPIException as e:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail="Failed to create user: " + str(e), status_code=500)

    @staticmethod
    def retrieve_instance(instance_id):
        try:
            return UserRepository.get_instance_by_id(instance_id)
        except CustomAPIException as e:
            raise
        except Exception as e:
            raise CustomAPIException(detail=str(e), status_code=500)

    @staticmethod
    def update_instance_and_partial_update(instance_id, validated_data):
        try:
            return UserRepository.update_instance(instance_id, validated_data)
        except CustomAPIException as e:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail="Failed to update user: " + str(e), status_code=500)

    @staticmethod
    def destroy_instance(instance_id):
        try:
            user = UserRepository.get_instance_by_id(instance_id)
            UserRepository.delete_instance(instance_id)
        except CustomAPIException as e:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail="Failed to delete user: " + str(e), status_code=500)
