from rest_framework import serializers
from ..models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("id", "user", "street", "city", 'state', 'number', 'neighborhood',
                  'complement', 'reference_point', 'zip_code', 'is_default')

    def if_default_is_true_update_for_false(self, validated_data):
        if "is_default" in validated_data and validated_data["is_default"] == True:
            Address.objects.filter(
                user=validated_data['user'], is_default=True).update(is_default=False)

    def create(self, validated_data):
        self.if_default_is_true_update_for_false(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.if_default_is_true_update_for_false(validated_data)
        return super().update(instance, validated_data)
