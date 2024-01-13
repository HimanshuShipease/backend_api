from rest_framework import serializers
from django.db import models
from dashboardapp.models import Orders
from billing_app.models import Transactions,CodTransactions


class ShipmentChargeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class RechargeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'        


class RemitenceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodTransactions
        fields = '__all__' 