from apps.shared.base_service import BaseService
from apps.shared.custom_api_exception import CustomAPIException
from .repository import AddressRepository


class AddressService(BaseService):

    @staticmethod
    def list_all_instances():
        try:
            return AddressRepository.get_all_instances()
        except CustomAPIException as e:
            raise
        except Exception as e:
            raise CustomAPIException(detail=str(e), status_code=500)

    @staticmethod
    def create_instance(validated_data):
        try:
            AddressService._if_default_is_true_update_for_false(validated_data)
            return AddressRepository.create_instance(validated_data)
        except CustomAPIException as e:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail="Failed to create address: " + str(e), status_code=500)

    @staticmethod
    def retrieve_instance(instance_id):
        try:
            return AddressRepository.get_instance_by_id(instance_id)
        except CustomAPIException as e:
            raise
        except Exception as e:
            raise CustomAPIException(detail=str(e), status_code=500)

    @staticmethod
    def update_and_partial_update_instance(instance_id, validated_data):
        try:
            AddressService._if_default_is_true_update_for_false(validated_data)
            return AddressRepository.update_instance(instance_id, validated_data)
        except CustomAPIException as e:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail="Failed to update address: " + str(e), status_code=500)

    @staticmethod
    def destroy_instance(instance_id):
        try:
            address = AddressRepository.get_instance_by_id(instance_id)
            AddressRepository.delete_instance(instance_id)
        except CustomAPIException as e:
            raise
        except Exception as e:
            raise CustomAPIException(
                detail="Failed to delete address: " + str(e), status_code=500)

    @staticmethod
    def _if_default_is_true_update_for_false(validated_data):
        if "is_default" in validated_data and validated_data["is_default"] == True:
            for address in AddressService.list_all_instances_for_user(validated_data['user']):
                AddressRepository.update_instance(
                    address.id, {'is_default': False})

    @staticmethod
    def list_all_instances_for_user(user_id):
        try:
            return AddressRepository.get_all_instances_for_user()
        except CustomAPIException as e:
            raise
        except Exception as e:
            raise CustomAPIException(detail=str(e), status_code=500)
