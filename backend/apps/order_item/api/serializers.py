from rest_framework import serializers
from apps.order_item.models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields= "__all__"
    
    def get_total_price(self, obj):
        product_price = 0.00
        if(obj.quantity):
            product_price = obj.quantity * obj.product.price
        return product_price
