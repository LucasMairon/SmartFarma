from rest_framework import viewsets
from .serializers import ProductSerializer
from apps.product.models import Product
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        permissions = [AllowAny]
        if self.action not in ['retrieve', 'list']:
            permissions = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permissions]