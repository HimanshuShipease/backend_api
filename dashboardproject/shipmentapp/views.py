from django.shortcuts import render
from dashboardapp.models import Orders,NdrAttemps
from shipmentapp.serializers import ActionRequestedSerializer,CombinedSerializer,NdrAttemptsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.db.models import Count
global_seller_id=16

#ndr raised Api
class NdrRaisedApi(APIView):
    def get(self, request, format=None):
        snippets =  Orders.objects.filter(ndr_status='y', 
                                          rto_status='n',
                                          seller_id=global_seller_id)
        ndr_raised_count =  Orders.objects.filter(ndr_status='y', 
                                          rto_status='n',
                                          seller_id=global_seller_id).count()
        serializer = ActionRequestedSerializer(snippets, many=True)
        response_data = {
            'ndr_raised_count': ndr_raised_count,
            'shipment_data': serializer.data,
        }
        return Response(response_data)

# action rewuested api
class ActionRequestedApi(APIView):
    def get(self, request, format=None):
        snippets =  Orders.objects.filter(ndr_status='y', ndr_action='requested',seller_id=global_seller_id)
        action_requested_count =  Orders.objects.filter(ndr_status='y', ndr_action='requested',seller_id=global_seller_id)
        serializer = ActionRequestedSerializer(snippets, many=True)
        response_data = {
            'action_requested_count': action_requested_count,
            'shipment_data': serializer.data,
        }
        return Response(response_data)
    
#api for action requried
class ActionReqApi(APIView):
    def get(self, request, format=None):
        snippets =  Orders.objects.filter(ndr_status='y', ndr_action='pending',seller_id=global_seller_id)
        action_req=Orders.objects.filter(ndr_status='y', ndr_action='pending',seller_id=global_seller_id).count()
       
        serializer = ActionRequestedSerializer(snippets, many=True)
        response_data = {
            'action_req': action_req,
            'shipment_data': serializer.data,
        }
        return Response(response_data)

## deleverd ndr section 
class Deleverdndrapi(APIView):
    def get(self, request, format=None):
        snippets =  Orders.objects.filter(ndr_status='y', ndr_action='delivered',seller_id=global_seller_id)
        deleverd_count =  Orders.objects.filter(ndr_status='y', ndr_action='delivered',seller_id=global_seller_id).count()
        serializer = ActionRequestedSerializer(snippets, many=True)
        response_data = {
            'deleverd_count': deleverd_count,
            'shipment_data': serializer.data,
        }
        return Response(response_data)

# RTO shipment
class Rtoshipmentapi(APIView):
    def get(self, request, format=None):
        snippets =  Orders.objects.filter(ndr_status='y',rto_status='y',
                                          seller_id=global_seller_id)
        count_rto_shipment =  Orders.objects.filter(ndr_status='y',rto_status='y',
                                          seller_id=global_seller_id).count()
        serializer = ActionRequestedSerializer(snippets, many=True)
        response_data = {
            'count_rto_shipment': count_rto_shipment,
            'shipment_data': serializer.data,
        }
        return Response(response_data)


class ActionRequestedApi_ogg(APIView):
    def get(self, request, format=None):
        global_seller_id = 14366
        set_date = timezone.now() - timezone.timedelta(days=80)
        last_30_days_orders = Orders.objects.filter(ndr_status='y', ndr_action='requested')
        order_ids = last_30_days_orders.values_list('id', flat=True)
        last_30_days_ndr_attempts = NdrAttemps.objects.filter(order_id__in=order_ids)
        ndr_attempts_count_per_order = last_30_days_ndr_attempts.values('order_id').annotate(ndr_attempts_count=Count('order_id'))
        ndr_attempts_data = {order_id: [] for order_id in order_ids}
        for ndr_attempt in last_30_days_ndr_attempts:
            ndr_attempts_data[ndr_attempt.order_id].append(NdrAttemptsSerializer(ndr_attempt).data)
        response_data = [
            {
                **CombinedSerializer(order).data,
                'ndr_attempts_data': ndr_attempts_data.get(order.id, []),
                
            }
            for order in last_30_days_orders
        ]
        return Response(response_data, status=status.HTTP_200_OK)
 