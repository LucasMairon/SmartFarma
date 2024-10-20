from rest_framework import serializers
from ..models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("id", "user", "street", "city", 'state', 'number', 'neighborhood',
                  'complement', 'reference_point', 'zip_code', 'is_default')


class AddressUserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("street", "city", 'state', 'number', 'neighborhood',
                  'complement', 'reference_point', 'zip_code')
