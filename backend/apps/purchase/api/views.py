from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.purchase.models import Purchase
from .serializers import PurchaseSerializer
from apps.purchase.service import PurchaseService
from rest_framework.response import Response
from rest_framework import status
from apps.shared.custom_api_exception import CustomAPIException


class PurchaseModelViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            purchase = PurchaseService.list_all_instances()
            return Response(PurchaseSerializer(purchase, many=True).data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            purchase = PurchaseService.create_instance(serializer.validated_data)
            return Response(PurchaseSerializer(purchase).data, status=status.HTTP_201_CREATED)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
        
    def retrieve(self, request, pk=None):
        try:
            purchase = PurchaseService.retrieve_instance(pk)
            return Response(PurchaseSerializer(purchase).data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
        
    def update(self, request, pk=None):
        try:
            purchase = PurchaseService.retrieve_instance(pk)
            serializer = self.get_serializer(
                purchase, data=request.data, partial=False
            )
            serializer.is_valid(raise_exception=True)
            purchase = PurchaseService.update_instance_and_partial_update(pk, serializer.validated_data)
            return Response(PurchaseSerializer(purchase).data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
        
    def partial_update(self, request, pk=None):
        try:
            purchase = PurchaseService.retrieve_instance(pk)
            serializer = self.get_serializer(
                purchase, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            purchase = PurchaseService.update_instance_and_partial_update(pk, serializer.validated_data)
            return Response(PurchaseSerializer(purchase).data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
        
    def destroy(self, request, pk=None):
        try: 
            PurchaseService.destroy_instance(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)