from rest_framework import viewsets
from apps.order_item.models import OrderItem
from apps.order_item.api.serializers import OrderItemSerializer, OrderItemCreateAndpdateSerializer
from rest_framework.permissions import IsAuthenticated
from apps.order_item.service import OrderItemService
from rest_framework.response import Response
from apps.shared.custom_api_exception import CustomAPIException
from rest_framework import status


class OrderItemModelViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action not in ('list', 'retrieve'):
            return OrderItemCreateAndpdateSerializer
        return OrderItemSerializer

    def list(self, request):
        try:
            order_item = OrderItemService.list_all_instances()
            return Response(OrderItemSerializer(order_item, many=True).data,
                            status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            order_item = OrderItemService.create_instance(
                serializer.validated_data)
            return Response(OrderItemSerializer(order_item).data,
                            status=status.HTTP_201_CREATED)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def retrieve(self, request, pk=None):
        try:
            order_item = OrderItemService.retrieve_instance(pk)
            return Response(OrderItemSerializer(order_item).data,
                            status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def update(self, request, pk=None):
        try:
            order_item = OrderItemService.retrieve_instance(pk)
            serializer = self.get_serializer(
                order_item, data=request.data, partial=False
            )
            serializer.is_valid(raise_exception=True)
            order_item = OrderItemService.update_instance_and_partial_update(
                pk, serializer.validated_data
            )
            return Response(OrderItemSerializer(order_item).data,
                            status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def partial_update(self, request, pk=None):
        try:
            order_item = OrderItemService.retrieve_instance(pk)
            serializer = self.get_serializer(
                order_item, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            order_item = OrderItemService.update_instance_and_partial_update(
                pk, serializer.validated_data
            )
            return Response(OrderItemSerializer(order_item).data,
                            status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)

    def destroy(self, request, pk=None):
        try:
            OrderItemService.destroy_instance(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
