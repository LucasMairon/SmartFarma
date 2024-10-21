from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'cpf', 'date_of_birth',
                  'phone_number', "street", "city", 'state', 'number',
                  'neighborhood', 'complement', 'reference_point',
                  'zip_code', 'password')