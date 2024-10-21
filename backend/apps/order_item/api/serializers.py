from rest_framework import serializers
from apps.order_item.models import OrderItem
from apps.product.api.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField(method_name="get_total_price")
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ("quantity", 'price', "product")

    def get_total_price(self, obj):
        product_price = 0.00
        if (obj.quantity):
            product_price = obj.quantity * obj.product.price
        return product_price


class OrderItemCreateAndpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("quantity", "product", "cart")

