from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Address
from .serializers import AddressSerializer
from ..service import AddressService


class AddressModelViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            addresss = AddressService.list_all_instances()
            return Response(AddressSerializer(addresss, many=True).data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            address = AddressService.create_instance(serializer.validated_data)
            return Response(AddressSerializer(address).data, status=status.HTTP_201_CREATED)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def retrieve(self, request, pk=None):
        try:
            address = AddressService.retrieve_instance(pk)
            return Response(AddressSerializer(address).data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def update(self, request, pk=None):
        try:
            address = AddressService.retrieve_instance(pk)
            serializer = self.get_serializer(
                address, data=request.data, partial=False)
            serializer.is_valid(raise_exception=True)
            address = AddressService.update_instance_and_partial_update(
                pk, serializer.validated_data)
            return Response(AddressSerializer(address).data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def partial_update(self, request, pk=None):
        try:
            address = AddressService.retrieve_instance(pk)
            serializer = self.serializer_class(
                address, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            address = AddressService.update_instance_and_partial_update(
                pk, serializer.validated_data)
            return Response(AddressSerializer(address).data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def destroy(self, request, pk=None):
        try:
            AddressService.destroy_instance(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
