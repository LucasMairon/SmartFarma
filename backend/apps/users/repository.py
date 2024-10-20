from apps.shared.base_repositoy import BaseRepository
from .models import CustomUser
from apps.shared.custom_api_exception import CustomAPIException


class UserRepository(BaseRepository):

    @staticmethod
    def create_instance(validated_data):
        return CustomUser.objects.create_user(**validated_data)

    @staticmethod
    def get_all_instances():
        return CustomUser.objects.all()

    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            return CustomUser.objects.get(id=instance_id)
        except CustomUser.ObjectDoesNotExist:
            raise CustomAPIException(
                detail='User not found.', status_code=404)

    @staticmethod
    def update_instance(instance_id, validated_data):

        try:
            user = CustomUser.objects.get(id=instance_id)

            if 'password' in validated_data:
                user.set_password(validated_data['password'])
                del validated_data['password']

            for attr, value in validated_data.items():
                setattr(user, attr, value)

            user.save()
            return user
        except CustomUser.ObjectDoesNotExist:
            raise CustomAPIException("User not found",  status_code=404)

    @staticmethod
    def delete_instance(instance_id):
        try:
            user = CustomUser.objects.get(id=instance_id)
            user.delete()
        except CustomUser.ObjectDoesNotExist:
            raise CustomAPIException("User not found",  status_code=404)
