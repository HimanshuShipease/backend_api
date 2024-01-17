from rest_framework import serializers
from django.db import models
from dashboardapp.models import Orders
from billing_app.models import Transactions,CodTransactions,Invoice,BillReceipt


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


class InvoiceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__' 

class PassbookLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__' 

class BillingReceptLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillReceipt
        fields = '__all__' 
