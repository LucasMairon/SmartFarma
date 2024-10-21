from rest_framework import serializers
from apps.order_item.api.serializers import OrderItemSerializer
from ..models import Cart


class CartSerializer(serializers.ModelSerializer):

    total_price = serializers.SerializerMethodField()
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'total_price', 'order_items')

    def get_total_price(self, obj):
        order_items = obj.order_items.all()
        total_price = 0.00
        for item in order_items:
            total_price += item.price
        return total_price
