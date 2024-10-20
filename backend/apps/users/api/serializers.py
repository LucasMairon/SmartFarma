from django.contrib.auth import get_user_model
from rest_framework import serializers
from apps.address.api.serializers import AddressSerializer, AddressUserCreateSerializer
from apps.address.models import Address

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'cpf', 'date_of_birth',
                  'phone_number', 'addresses')


class UserCreateSerializer(serializers.ModelSerializer):

    address = AddressUserCreateSerializer()

    class Meta:
        model = User
        fields = ('name', 'email', 'cpf', 'date_of_birth',
                  'phone_number', 'address', 'password')


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'email', 'cpf', 'date_of_birth',
                  'phone_number', 'password')
