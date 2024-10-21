from apps.shared.base_repositoy import BaseRepository
from apps.shared.custom_api_exception import CustomAPIException
from .models import Purchase

class PurchaseRepository(BaseRepository):

    @staticmethod
    def create_instance(validated_data):
        return Purchase.objects.create(**validated_data)
    
    @staticmethod
    def get_all_instances():
        return Purchase.objects.all()
    
    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            return Purchase.objects.get(id=instance_id)
        except Purchase.DoesNotExist:
            raise CustomAPIException(
                detail='purchase not found', status_code=404
            )
        
    @staticmethod
    def update_instance(instance_id, validated_data):
        try:
            purchase = Purchase.objects.get(id=instance_id)
            for attr, value in validated_data.items():
                setattr(purchase, attr, value)
            purchase.save()
            return purchase
        except Purchase.DoesNotExist:
            raise CustomAPIException(
                'purchase not found', status_code=404
            )
        
    @staticmethod
    def delete_instance(instance_id):
        try:
            purchase = Purchase.objects.get(id=instance_id)
            purchase.delete()
        except Purchase.DoesNotExist:
            raise CustomAPIException(
                'purchase not found', status_code=404
            )