from apps.shared.base_repositoy import BaseRepository
from .models import Product
from apps.shared.custom_api_exception import CustomAPIException

class ProductRepository(BaseRepository):

    @staticmethod
    def create_instance(**validated_data):
        return Product.objects.create(**validated_data)

    @staticmethod
    def get_all_instances():
        return Product.objects.all()
    
    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            return Product.objects.get(id=instance_id)
        except Product.DoesNotExist:
            raise CustomAPIException(
                detail='product not found', status_code=404
            )
    
    @staticmethod
    def update_instance(instance_id, **validated_data):
        try:
            product = Product.objects.get(id=instance_id)
            for attr, value in validated_data.items():
                setattr(product, attr, value)
            product.save()
            return product
        except Product.DoesNotExist:
            raise CustomAPIException(
                'product not found', status_code=404
            )
        
    @staticmethod
    def delete_instance(instance_id):
        try:
            product = Product.objects.get(id=instance_id)
            product.delete()
        except Product.DoesNotExist:
            raise CustomAPIException(
                'product not found', status_code=404
            )
    