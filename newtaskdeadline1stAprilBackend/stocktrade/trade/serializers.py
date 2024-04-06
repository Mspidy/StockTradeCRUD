from rest_framework import serializers
from .models import Trade, OrderDetails

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'