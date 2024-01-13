from django.shortcuts import render
from dashboardapp.models import Orders
from .models import Transactions
from billing_app.serializers import ShipmentChargeOrderSerializer,RechargeLogSerializer,RemitenceLogSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.db.models.functions import Cast
from django.db.models import IntegerField

global_seller_id=16

###api for shipment log
class ShipingChargesApi(APIView):
    def get(self, request, format=None):
        snippets = Orders.objects.filter(shipping_charges__isnull=False)[:30]
        # Convert total_charges to IntegerField and then apply Sum
        Total_freight_charges = Orders.objects.exclude(status__in=['pending', 'cancelled']).aggregate(
            total_charges_sum=Cast(Sum('total_charges'), IntegerField())
        )
        serializer = ShipmentChargeOrderSerializer(snippets, many=True)
        response_data = {
            'Total_freight_charges': Total_freight_charges['total_charges_sum'],
            'shipment_data': serializer.data,
        }
        return Response(response_data)


class RemitenceLog (APIView):
    def get(self, request, format=None):
        snippets = Transactions.objects.all()[:30]
        serializer = RemitenceLogSerializer(snippets, many=True)
        return Response(serializer.data)


class RechargeLogs (APIView):
    def get(self, request, format=None):
        snippets = Transactions.objects.filter(redeem_type='r')[:30]
        serializer = RechargeLogSerializer(snippets, many=True)
        return Response(serializer.data)




