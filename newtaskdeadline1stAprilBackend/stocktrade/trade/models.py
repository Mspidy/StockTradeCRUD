from django.db import models

class Trade(models.Model):
    tradeDateTime = models.DateTimeField()
    stockName = models.CharField(max_length=100)
    listingPrice = models.IntegerField()
    quantity = models.IntegerField()
    type = models.CharField(max_length=4, choices=(('buy', 'Buy'), ('sell', 'Sell')))
    pricePerUnit = models.IntegerField()

class OrderDetails(models.Model):
    order_id = models.AutoField(primary_key=True)
    stockName = models.CharField(max_length=100)
    quantity = models.IntegerField()
    listingPrice = models.IntegerField()
    status = models.CharField(max_length=100, default="confirmed")
    # Add more fields as needed
