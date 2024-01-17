from django.shortcuts import render
from dashboardapp.models import Orders,NdrAttemps,Products
from dashboardapp.serializers import FetchAllOrdersSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.db.models import Count
from datetime import timedelta
from django.utils import timezone
from orderapp.serializers import CreateOrdersSerializer
global_seller_id=16

# Create your views here.
from django.http import Http404

class FetchAllOrdersDetail(APIView):
    def get(self, request, format=None):
        try:
            set_date = timezone.now() - timezone.timedelta(days=30)
            snippets = Orders.objects.filter(seller_id=16, inserted__date=set_date)
            serializer = FetchAllOrdersSerializer(snippets, many=True)
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FetchAllOrdersDetailById(APIView):
    def get_object(self, pk):
        try:
            return Orders.objects.get(pk=pk)
        except Orders.DoesNotExist:
            raise Http404("Order not found")

    def get(self, request, pk, format=None):
        try:
            snippet = self.get_object(pk)
            serializer = FetchAllOrdersSerializer(snippet)
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        except Http404 as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.db.models.functions import Length
from django.db.models import Q, CharField, Value

class UnprocessableOrder(APIView):
    def filter_unprocessable_order_data(self, queryset):
        match_conditions = Q(
            product_name='',
            product_sku='',
            s_customer_name='',
            s_address_line1='',
            s_country='',
            s_state='',
            s_city='',
            s_pincode='',
            s_contact='',
            b_customer_name='',
            b_address_line1='',
            b_country='',
            b_state='',
            b_city='',
            b_pincode='',
            b_contact='',
            weight='',
            length='',
            breadth='',
            height='',
            invoice_amount='',
            weight__isnull=True,
            breadth__isnull=True,
            height__isnull=True,
            invoice_amount__isnull=True
        )
        annotated_queryset = queryset.annotate(
            b_contact_length=Length('b_contact'),
            b_pincode_length=Length('b_pincode', output_field=CharField())
        )
        return annotated_queryset.filter(
            Q(match_conditions) |
            (
                (Q(invoice_amount=0) | Q(b_contact__isnull=True) | Q(b_contact='9999999999') | ~Q(b_contact_length=10)) |
                ~Q(b_pincode_length=6)
            )
        ).filter(status='pending')
    
    # seller_id=global_seller_id
    def get(self, request, format=None):
        queryset = Orders.objects.filter(seller_id=global_seller_id)
        filtered_orders = self.filter_unprocessable_order_data(queryset)
        count_number = filtered_orders.count() 
        response_data = {
            'filtered_orders': filtered_orders.values(),
            'count_number':count_number
        }
        return Response(response_data, status=status.HTTP_200_OK)

# processable order in order section
class ProcessableOrder(APIView):
    def filter_unprocessable_order_data(self, queryset):
        match_conditions = Q(
            product_name__isnull=False,
            product_sku__isnull=False,
            s_customer_name__isnull=False,
            s_address_line1__isnull=False,
            s_country__isnull=False,
            s_state__isnull=False,
            s_city__isnull=False,
            s_pincode__isnull=False,
            s_contact__isnull=False,
            b_customer_name__isnull=False,
            b_address_line1__isnull=False,
            b_country__isnull=False,
            b_state__isnull=False,
            b_city__isnull=False,
            b_pincode__isnull=False,
            b_contact__isnull=False,
            weight__isnull=False,
            length__isnull=False,
            height__isnull=False,
            breadth__isnull=False,
            invoice_amount__isnull=False
        )
        return queryset.filter(
            Q(match_conditions) | Q(status='pending')
        )

    def get(self, request, format=None):
        thirty_days_ago = timezone.now() - timedelta(days=30)

        # Filtering orders for the last 30 days with status 'pending'
        data = Orders.objects.filter(
            Q(status='pending') &
            # Q(seller_id=global_seller_id) &
            Q(inserted__gte=thirty_days_ago)
        )

        # Applying match_conditions on the filtered data
        processable_order = self.filter_unprocessable_order_data(data)
        count_number = processable_order.count()

        # Prepare the response data
        response_data = {
            'processable_order': processable_order.values(),
            'count_number': count_number
        }

        # Return the response with a status code of 200 (OK)
        return Response(response_data, status=status.HTTP_200_OK)
# pickup request api in order
class ReadyToShipOrder(APIView):
    def get(self, request, format=None):
        snippets = Orders.objects.filter(
            Q(manifest_status='y') &
            (Q(status='pickup_requested') | Q(status='shipped')) &
            Q(seller_id=global_seller_id)
        )
        serializer = FetchAllOrdersSerializer(snippets, many=True)
        return Response(serializer.data)

# return order api in order tab
class ReturnOrder(APIView):
    def get(self, request, format=None):
        snippets = Orders.objects.filter(rto_status='y', seller_id=global_seller_id)                    
        serializer = FetchAllOrdersSerializer(snippets, many=True)
        return Response(serializer.data)
    

#create new order section here
class CreateOrderapi(APIView):
    serializer_class = CreateOrdersSerializer

    def post(self, request, format=None):
        serializer = CreateOrdersSerializer(data=request.data, partial=True)
        get_weight = float(request.data.get('weight', 0))  # Default to 0 if 'weight' is not provided
        get_length = float(request.data.get('length', 0))
        get_breadth = float(request.data.get('breadth', 0))
        get_height = float(request.data.get('height', 0))
      
        vol_weight = (get_weight * get_length * get_breadth * get_height) / 5000
        print("val weight is", vol_weight)

        if serializer.is_valid():
            serializer.save(channel='custom', seller_id=16, warehouse_id=42, vol_weight=vol_weight, last_sync='2023-12-13T19:45:27Z')
            last_order = Orders.objects.filter(seller_id=16).latest('inserted')
            product_order_id = last_order.id
            product_sku = last_order.product_sku
            product_name = last_order.product_name
            product_quantity = last_order.product_qty
            create_product = Products.objects.create(order_id=product_order_id,
                                                    product_sku=product_sku,
                                                    product_name=product_name,
                                                    product_qty=product_quantity,
                                                    item_id=product_order_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
