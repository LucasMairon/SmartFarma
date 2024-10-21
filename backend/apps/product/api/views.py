from rest_framework import viewsets
from .serializers import ProductSerializer
from apps.product.models import Product
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from apps.shared.custom_api_exception import CustomAPIException
from rest_framework.response import Response
from apps.product.service import ProductService
from rest_framework import status

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        permissions = [AllowAny]
        if self.action not in ['retrieve', 'list']:
            permissions = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permissions]
    
    def list(self, request):
        try:
            product = ProductService.list_all_instances()
            return Response(ProductSerializer(product, many=True).data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try: 
            product = ProductService.create_instance(serializer.validated_data)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
        
    def retrieve(self, request, pk=None):
        try:
            product = ProductService.retrieve_instance(pk)
            return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
    
    def update(self, request, pk=None):
        try:
            product = ProductService.retrieve_instance(pk)
            serializer = self.get_serializer(
                product, data=request.data, partial=False
            )
            serializer.is_valid(raise_exception=True)
            product = ProductService.update_instance_and_partial_update(
                pk, serializer.validated_data
            )
            return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
        
    def partial_update(self, request, pk=None):
        try:
            product = ProductService.retrieve_instance(pk)
            serializer = self.get_serializer(
                product, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            product = ProductService.update_instance_and_partial_update(
                pk, serializer.validated_data
            )
            return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
        
    def destroy(self, request, pk=None):
        try:
            ProductService.destroy_instance(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
        