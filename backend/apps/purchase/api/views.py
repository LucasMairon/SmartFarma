from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.purchase.models import Purchase
from .serializers import PurchaseSerializer

class PurchaseModelViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]