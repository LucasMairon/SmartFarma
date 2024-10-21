from rest_framework import viewsets
from .serializers import CartSerializer
from ..models import Cart
from ..service import CartService
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.shared.custom_api_exception import CustomAPIException


class CartGenericAPIView(viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='retrieve-or-create')
    def retrieve_or_create(self, request):
        try:
            cart = CartService.get_or_create(request.user.id)
            serializer = self.get_serializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomAPIException as e:
            return Response({"detail": str(e)}, status=e.status_code)
