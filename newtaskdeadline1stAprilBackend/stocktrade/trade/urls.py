# urls.py

from django.urls import path
from .views import TradeAPIView, OrderAPIView

urlpatterns = [
    path('api/trades/', TradeAPIView.as_view(), name='trade_api'),
    path('api/trades/<int:pk>/', TradeAPIView.as_view(), name='trade_detail_api'),
    path('api/order/', OrderAPIView.as_view(), name='order_api')
]
