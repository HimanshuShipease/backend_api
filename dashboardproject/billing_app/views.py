from django.shortcuts import render
from dashboardapp.models import Orders
from .models import Transactions,CodTransactions,Invoice,Sellers,BillReceipt
from billing_app.serializers import (ShipmentChargeOrderSerializer,
                                     RechargeLogSerializer,
                                     RemitenceLogSerializer,
                                     InvoiceLogSerializer,
                                     PassbookLogSerializer,
                                     BillingReceptLogSerializer
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.db.models.functions import Cast
from django.db.models import IntegerField
from datetime import datetime, timedelta

global_seller_id=16

###api for shipment log
class ShipingChargesApi(APIView):
    def get(self, request, format=None):
        global_seller_id = 14366

        # Calculate the date one month ago
        one_month_ago = datetime.now() - timedelta(days=25)

        # Fetch snippets with shipping charges for the last 25 days
        snippets = Orders.objects.filter(
            seller_id=global_seller_id,
            shipping_charges__isnull=False,
            inserted__gte=one_month_ago
        )[:30]  # You may want to adjust the number of items to retrieve

        # Calculate total freight charges excluding pending and cancelled orders
        total_freight_charges = Orders.objects.filter(
            seller_id=global_seller_id
        ).exclude(status__in=['pending', 'cancelled']).aggregate(
            total_charges_sum=Cast(Sum('total_charges'), IntegerField())
        )['total_charges_sum'] or 0

        # Serialize the snippets
        serializer = ShipmentChargeOrderSerializer(snippets, many=True)

        # Prepare the response data
        response_data = {
            'Total_freight_charges': total_freight_charges,
            'shipment_data': serializer.data,
        }

        return Response(response_data)


class RemitenceLog (APIView):
    def get(self, request, format=None):
        # one_month_ago = datetime.now() - timedelta(days=50)
        snippets = CodTransactions.objects.all()[:30]


        total_cod=Orders.objects.filter (seller_id=global_seller_id,order_type='cod',status='Delivered', rto_status='n').aggregate(
            total_cod_sum=Cast(Sum('invoice_amount'), IntegerField())) 
        cod_remited=Orders.objects.filter (seller_id=global_seller_id,order_type='cod',status='Delivered', rto_status='n',cod_remmited='y').aggregate(
            total_cod_remited=Cast(Sum('invoice_amount'), IntegerField()))
        cod_pending=Orders.objects.filter (seller_id=global_seller_id,order_type='cod',status='Delivered', rto_status='n',cod_remmited='n').aggregate(
            total_cod_pending=Cast(Sum('invoice_amount'), IntegerField()))                                             
        serializer = RemitenceLogSerializer(snippets, many=True)
        remittance_days = Sellers.objects.get(id=global_seller_id).remmitance_days
        total_remidence_blance=Orders.objects.filter(seller_id=global_seller_id).aggregate(
            total_cod_remited_blc=Cast(Sum('invoice_amount'), IntegerField()))
        
        response_data = {
            'Total_cod_charges': total_cod['total_cod_sum'],
            'cod_remited':cod_remited['total_cod_remited'],
            'cod_pending':cod_pending['total_cod_pending'],
            'remited_day':remittance_days,
            'total_remidence_blance':total_remidence_blance['total_cod_remited_blc'],
            'shipment_data': serializer.data,
        }
        return Response(response_data)



class RechargeLogs (APIView):
    def get(self, request, format=None):
        snippets = Transactions.objects.filter(redeem_type='r')[:30]
        total_sucefully_recharge=Transactions.objects.filter(redeem_type='r').aggregate(
            sucefully_recharge_sum=Cast(Sum('amount'), IntegerField()))

        total_credit=Transactions.objects.filter(redeem_type='r',type='c').aggregate(
            total_credit_sum=Cast(Sum('balance'), IntegerField()))
        
        total_devit=Transactions.objects.filter(redeem_type='r',type='d').aggregate(
            total_devit_sum=Cast(Sum('balance'), IntegerField()))
         
        serializer = RechargeLogSerializer(snippets, many=True)
        response_data = {
            'total_sucefully_recharge': total_sucefully_recharge['sucefully_recharge_sum'],
            'total_credit':total_credit['total_credit_sum'],
            'total_devit':total_devit['total_devit_sum'],
            'recharge_log': serializer.data,
        }
        return Response(response_data)

class InvoiceLog (APIView):
    def get(self, request, format=None):
        snippets = Invoice.objects.all()
        other_serializer=Invoice.objects.filter(type='o')
        serializer = InvoiceLogSerializer(snippets, many=True)
        other_serializer=InvoiceLogSerializer(other_serializer, many=True)
        response_data = {
            'invoice_log': serializer.data,
            'other_serializer':other_serializer.data
        }
        return Response(response_data)
    

class PassbookLog(APIView):
    def get(self, request, format=None):
        passbooklog = Transactions.objects.filter(seller_id=global_seller_id, type='o')
        corrent_blance = Sellers.objects.get(id=global_seller_id).balance
        current_unavailable_balance = float(corrent_blance) - 200
        corrent_on_hold_blance = Sellers.objects.get(id=global_seller_id).onhold_balance

        serializer = PassbookLogSerializer(passbooklog, many=True)
        response_data = {
            'current_unavailable_balance': current_unavailable_balance,
            'corrent_on_hold_blance': corrent_on_hold_blance,
            'corrent_blance': corrent_blance,
            'passbook_log': serializer.data,
        }
        return Response(response_data)  
    
# 
class CreditReceptLog(APIView):
    def get(self, request, format=None):
        creditrecept = BillReceipt.objects.filter(seller_id=global_seller_id)
        serializer = BillingReceptLogSerializer(creditrecept, many=True)
        response_data = {
            'cerdit_recept_log': serializer.data,
        }
        return Response(response_data)      