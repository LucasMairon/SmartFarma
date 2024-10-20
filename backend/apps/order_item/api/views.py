from rest_framework import viewsets
from apps.order_item.models import OrderItem
from apps.order_item.api.serializers import OrderItemSerializer
from rest_framework.permissions import IsAuthenticated

class OrderItemModelViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

