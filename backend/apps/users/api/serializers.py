from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'cpf', 'date_of_birth',
                  'phone_number', 'access_level')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'cpf', 'date_of_birth',
                  'phone_number', 'access_level', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = User.objects.create_user(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.date_of_birth = validated_data.get(
            'date_of_birth', instance.date_of_birth)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.access_level = validated_data.get(
            'access_level', instance.access_level)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance
