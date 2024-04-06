from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Trade, OrderDetails
from .serializers import TradeSerializer, OrderSerializer

class TradeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        trades = Trade.objects.all()
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        try:
            trade = Trade.objects.get(pk=pk)
        except Trade.DoesNotExist:
            return Response({"error": "Trade does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TradeSerializer(trade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            trade = Trade.objects.get(pk=pk)
        except Trade.DoesNotExist:
            return Response({"error": "Trade does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        trade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderAPIView(APIView):
    def get(self, request, *args, **kwargs):
        orders = OrderDetails.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
