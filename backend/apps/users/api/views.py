from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from ..service import UserService
from apps.shared.custom_api_exception import CustomAPIException
from .serializers import (
    UserSerializer,
)


User = get_user_model()


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permissions = []
        if self.action not in ['create']:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def list(self, request):
        try:
            users = UserService.list_all_instances()
            return Response(self.get_serializer(users, many=True).data,
                            status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = UserService.create_instance(serializer.validated_data)
            return Response(UserSerializer(user).data,
                            status=status.HTTP_201_CREATED)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def retrieve(self, request, pk=None):
        try:
            user = UserService.retrieve_instance(pk)
            return Response(self.get_serializer(user).data,
                            status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def update(self, request, pk=None):
        try:
            user = UserService.retrieve_instance(pk)
            serializer = self.get_serializer(
                user, data=request.data, partial=False)
            serializer.is_valid(raise_exception=True)
            user = UserService.update_instance_and_partial_update(
                pk, serializer.validated_data)
            return Response(UserSerializer(user).data,
                            status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def partial_update(self, request, pk=None):
        try:
            user = UserService.retrieve_instance(pk)
            serializer = self.serializer_class(
                user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            user = UserService.update_instance_and_partial_update(
                pk, serializer.validated_data)
            return Response(UserSerializer(user).data,
                            status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def destroy(self, request, pk=None):
        try:
            UserService.destroy_instance(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = RefreshToken(request.data.get('refresh_token'))
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
