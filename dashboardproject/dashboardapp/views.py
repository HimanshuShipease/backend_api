from django.db import models

from django.shortcuts import render
from django.db.models import Case, When,Value,IntegerField,FloatField,Q,Count,Func,DateField,F,ExpressionWrapper,fields,ExpressionWrapper,BooleanField
from datetime import datetime, timedelta
from django.db.models.expressions import RawSQL
from dashboardapp.models import Parentsidebar,Orders,OrderTracking,NdrAttemps
from dashboardapp.serializers import PsidebarSerializer,OrderTrackingSerializer,ChannelWiseOrderSerializer,ZoneWiseNdrOrdersSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models.functions import ExtractMonth,TruncDay,TruncWeek,TruncMonth,Cast
from decimal import Decimal
from django.utils import timezone


############### start order dashboard section here#################
class Psidebarlist(APIView):
    def get(self, request, format=None):
        snippets = Parentsidebar.objects.all()
        serializer = PsidebarSerializer(snippets, many=True)
        return Response(serializer.data)
# Api for calculatetotal delevrd order       
class Totalorderscount(APIView):
   def get(self, request, *args, **kwargs):
        total_orders_count = Orders.objects.count()
        return Response({'total_orders_count': total_orders_count}, status=status.HTTP_200_OK)
# Api for calculate total cancel order
class TotalCancelOrderCount(APIView):
    def get(self, request, *args, **kwargs):
        total_cancel_order_count = OrderTracking.objects.filter(status='CANCELLED').count()
        return Response({'total_cancel_order_count': total_cancel_order_count}, status=status.HTTP_200_OK)
#Api for calculate total delevery order
class TotalDeleverdOrderCount(APIView):
    def get(self, request, *args, **kwargs):
        total_Delivered_order_count = OrderTracking.objects.filter(status='Delivered').count()
        return Response({'total_Delivered_order_count': total_Delivered_order_count}, status=status.HTTP_200_OK)
#Api for calculate total return order
class TotalReturnToOriginOrderCount(APIView):
    def get(self, request, *args, **kwargs):
        total_return_to_origin_order_count = OrderTracking.objects.filter(status='Return to Origin').count()
        return Response({'total_return_to_origin_order_count': total_return_to_origin_order_count}, status=status.HTTP_200_OK)

# Api for calculate forword and backword order by month wise
class MonthlyOrders(APIView):
    def get(self, request, *args, **kwargs):
        start_month = request.query_params.get('start_month')
        end_month = request.query_params.get('end_month')
        if not start_month or not end_month:
            return Response({'error': 'Both start_month and end_month parameters are required.'}, status=status.HTTP_400_BAD_REQUEST)
        forward_orders = Orders.objects.filter(
            o_type='forward',
            inserted__month__range=[start_month, end_month]
        ).values('inserted__month').annotate(count=Count('id')).order_by('inserted__month')
        backward_orders = Orders.objects.filter(
            o_type='backward',
            inserted__month__range=[start_month, end_month]
        ).values('inserted__month').annotate(count=Count('id')).order_by('inserted__month')
        return Response({'forward_orders': forward_orders, 'backward_orders': backward_orders}, status=status.HTTP_200_OK)
#api for count total canceel order by month wise
class TotalCancelOrderGraph(APIView):
    def get(self, request, *args, **kwargs):
        start_month_str = request.query_params.get('start_month')
        end_month_str = request.query_params.get('end_month')

        # Ensure start_month and end_month are provided
        if not start_month_str or not end_month_str:
            return Response({'error': 'Both start_month and end_month parameters are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Parse start_month and end_month
            start_month = int(start_month_str)
            end_month = int(end_month_str)

            # Annotate the queryset with the extracted month and count orders for each month
            cancel_order_counts = OrderTracking.objects.filter(
                status='CANCELLED',
                created_at__month__range=[start_month, end_month]
            ).annotate(month=ExtractMonth('created_at')).values('month').annotate(total_cancel_order_count=Count('id')).order_by('month')

            # Format the response
            monthly_cancel_counts = [
                {
                    'total_cancel_order_count': cancel_order['total_cancel_order_count'],
                    'month': cancel_order['month'],
                }
                for cancel_order in cancel_order_counts
            ]
            return Response({'monthly_cancel_counts': monthly_cancel_counts}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error in TotalCancelOrderCount API: {e}")
            return Response({'error': f'An error occurred while processing the request: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# http://127.0.0.1:8000/api/v1/cancel-orders-graph/?start_month=1&end_month=6  
class ChannalWiseGraph(APIView):
    def get(self, request, format=None):
        # Get total count for all channels
        total_count = Orders.objects.count()

        # Get channel-wise data
        channel_data = Orders.objects.values('channel').annotate(
            total_orders=Count('id')
        )
        # Calculate percentage for each channel
        channel_percentage_data = [
            {
                'name': channel['channel'],
                'total_count': channel['total_orders'],
                'total_percentage': round((Decimal(channel['total_orders']) / Decimal(total_count)) * 100, 2),
            }
            for channel in channel_data
        ]
        return Response(channel_percentage_data)
# api count state wise data
class StateWiseData(APIView):
    def get(self, request, format=None):
        total_count = Orders.objects.count()
        p_state_data = Orders.objects.values('p_state').annotate(
            total_orders=Count('id')
        )
        p_state_percentage_data = [
            {
                'p_state': p_state['p_state'],
                'total_orders': p_state['total_orders'],
                'total_percentage': round((Decimal(p_state['total_orders']) / Decimal(total_count)) * 100, 2),
            }
            for p_state in p_state_data
        ]
        return Response(p_state_percentage_data)

#Api for count Domestic and International order type
class CountOrderType(APIView):
    def get(self, request, format=None):
        # Get total count for all orders
        total_count = Orders.objects.count()
        # Calculate the date 7 days ago from today
        seven_days_ago = datetime.now() - timedelta(days=7)
        # Get daily data based on global_type for the last 7 days
        daily_data = Orders.objects.filter(
            global_type='domestic',
            inserted__gte=seven_days_ago
        ).values(
            'global_type',
            day=TruncDay('inserted')
        ).annotate(
            total_orders=Count('id')
        )
        # Calculate percentage for the specified global_type
        daily_percentage_data = [
            {
                'global_type': daily['global_type'],
                'total_orders': daily['total_orders'],
                'day': daily['day'],
                # 'total_percentage': round((Decimal(daily['total_orders']) / Decimal(total_count)) * 100, 2),
            }
            for daily in daily_data
        ]
        return Response(daily_percentage_data)


class TopProductSKU(APIView):
    def get(self, request, format=None):
        # Get the top product SKUs based on order count
        top_product_skus = Orders.objects.values('product_sku').annotate(
            order_count=Count('id')
        ).order_by('-order_count')[:10]  # You can adjust the number as needed
        top_product_sku_data = [
            {
                'product_sku': product['product_sku'],
                'order_count': product['order_count'],
            }
            for product in top_product_skus
        ]

        return Response(top_product_sku_data)

#calculate sps and mps both 
class PopularSKUs(APIView):
    def get(self, request, format=None):
        # Calculate the date 7 days ago from today
        seven_days_ago = datetime.now() - timedelta(days=7)

        # Get most popular SKU (MPS) and least popular SKU (SPS) for the last 7 days
        mps_data = Orders.objects.filter(
            inserted__gte=seven_days_ago,
            shipment_type__isnull=False
        ).values('product_sku', day_of_week=TruncDay('inserted')).annotate(
            order_count=Count('id')
        ).order_by('-order_count')

        sps_data = Orders.objects.filter(
            inserted__gte=seven_days_ago,
            shipment_type__isnull=True
        ).values('product_sku', day_of_week=TruncDay('inserted')).annotate(
            order_count=Count('id')
        ).order_by('order_count')

        # Prepare the response data
        response_data = {
            'most_popular_sku': [
                {
                    'product_sku': mps['product_sku'],
                    'order_count': mps['order_count'],
                    'day_of_week': mps['day_of_week'].strftime('%A') if mps['day_of_week'] else None,
                }
                for mps in mps_data
            ] if mps_data else None,
            'least_popular_sku': [
                {
                    'product_sku': sps['product_sku'],
                    'order_count': sps['order_count'],
                    'day_of_week': sps['day_of_week'].strftime('%A') if sps['day_of_week'] else None,
                }
                for sps in sps_data
            ] if sps_data else None,
        }

        return Response(response_data)
##################### end order dashboard section here###########     


#########start Rto section here #############

class CalculateRto(APIView):
     def get(self, request, format=None):
        # Count total RTO orders
        total_rto_count = Orders.objects.filter(rto_status='y').count()

        # Get status-wise counts for RTO orders
        status_wise_counts = Orders.objects.filter(rto_status='y').values('status').annotate(
            status_count=Count('id')
        )

        # Calculate percentage for each status
        status_wise_percentages = [
            {
                'status': status['status'],
                'status_count': status['status_count'],
                'percentage': round((status['status_count'] / total_rto_count) * 100, 2) if total_rto_count else 0,
            }
            for status in status_wise_counts
        ]

        # Prepare the response data
        response_data = {
            'total_rto_count': total_rto_count,
            'status_wise_percentages': status_wise_percentages,
        }
        return Response(response_data)


class InTransitAndTransit(APIView):
    def get(self, request, format=None):
        # Calculate the date 30 days ago from today
        thirty_days_ago = datetime.now() - timedelta(days=30)

        # Get weekly counts for 'in_transit' status
        in_transit_data = Orders.objects.filter(
            status='in_transit',
            inserted__gte=thirty_days_ago
        ).annotate(
            week=TruncWeek('inserted')
        ).values('week').annotate(
            week_count=Count('id')
        ).order_by('week')

        # Get weekly counts for 'transit' status
        transit_data = Orders.objects.filter(
            status='transit',
            inserted__gte=thirty_days_ago
        ).annotate(
            week=TruncWeek('inserted')
        ).values('week').annotate(
            week_count=Count('id')
        ).order_by('week')

        # Combine weekly counts for both statuses
        combined_data = {}
        for data in in_transit_data:
            week_number = data['week'].isocalendar()[1]
            combined_data.setdefault(week_number, {'in_transit': 0, 'transit': 0})
            combined_data[week_number]['in_transit'] += data['week_count']

        for data in transit_data:
            week_number = data['week'].isocalendar()[1]
            combined_data.setdefault(week_number, {'in_transit': 0, 'transit': 0})
            combined_data[week_number]['transit'] += data['week_count']

        # Prepare the response data
        response_data = [
            {
                'week_number': week_number,
                'in_transit': data['in_transit'],
                'transit': data['transit'],
                'total': data['in_transit'] + data['transit'],
            }
            for week_number, data in combined_data.items()
        ]
        return Response(response_data)

#calculate top Rto city
class TopRTOCity(APIView):
    def get(self, request, format=None):
        # Get top RTO counts city-wise
        top_rto_city_data = Orders.objects.filter(
            rto_status='y'
        ).values('p_city').annotate(
            rto_count=Count('id')
        ).order_by('-rto_count')[:10]
        # Prepare the response data
        response_data = [
            {
                'city': data['p_city'],
                'rto_count': data['rto_count'],
            }
            for data in top_rto_city_data
        ]
        return Response(response_data)

#Api count top RTO pin wise and city wise
class TopRTOPinCode(APIView):
    def get(self, request, format=None):
        # Get top RTO counts city-wise
        top_rto_city_data = Orders.objects.filter(
            rto_status='y'
        ).values('p_city', 'p_pincode').annotate(
            city_name=F('p_city'),
            pincode=F('p_pincode'),
            rto_count=Count('id')
        ).order_by('-rto_count')[:10]  # Change the value inside [:10] to control the number of top cities

        # Prepare the response data
        response_data = [
            {
                'city_name': data['city_name'],
                'pincode': data['pincode'],
                'rto_count': data['rto_count'],
            }
            for data in top_rto_city_data
        ]
        return Response(response_data) 
#Rto count year wise month wise
class MonthlyRTOOrders(APIView):
    def get(self, request, format=None):
        # Calculate the date one year ago from today
        one_year_ago = datetime.now() - timedelta(days=365)
        # Get monthly RTO orders for the last one year
        monthly_rto_orders = Orders.objects.filter(
            rto_status='y',
            inserted__gte=one_year_ago
        ).annotate(
            month=TruncMonth('inserted')
        ).values('month').annotate(
            total_rto_orders=Count('id')
        ).order_by('month')

        # Prepare the response data
        response_data = [
            {
                'month': data['month'].strftime('%B'),
                'total_rto_orders': data['total_rto_orders'],
            }
            for data in monthly_rto_orders
        ]
        return Response(response_data)

#Api for top rto couriar pathner
class TopRTOPCouriarPathner(APIView):
    def get(self, request, format=None):
        # Get top RTO counts city-wise
        top_rto_city_data = Orders.objects.filter(
            rto_status='y'
        ).values('courier_partner').annotate(
            top_courier_partner=F('courier_partner'),
            rto_count=Count('id')
        ).order_by('-rto_count')[:5]
        response_data = [
            {
                'courier_partner': data['top_courier_partner'],
                'rto_count': data['rto_count'],
            }
            for data in top_rto_city_data
        ]
        return Response(response_data)

##### Rto section end here #######
##### ndr section start here ###########


#Api calculate total ndr
class CalculateTotalNdr(APIView):
     def get(self, request, format=None):
        # Count total RTO orders
        total_ndr_count = Orders.objects.filter(ndr_status='y').count()
        return Response({'total_ndr_count': total_ndr_count}, status=status.HTTP_200_OK)
#Api for calculate total requried ndr
class TotalRequiredNdr(APIView):
     def get(self, request, format=None):
        # Count total RTO orders
        total_ndr_count = Orders.objects.filter(ndr_action='pending').count()
        return Response({'total_ndr_count': total_ndr_count}, status=status.HTTP_200_OK)

#Api for calculate total requested ndr
class TotalRewuestedNdr(APIView):
     def get(self, request, format=None):
        # Count total RTO orders
        total_ndr_count = Orders.objects.filter(ndr_action='requested').count()
        return Response({'total_ndr_count': total_ndr_count}, status=status.HTTP_200_OK)

# Api for count total delevrd count ndr
class TotalDeleverdNdr(APIView):
    def get(self, request, format=None):
        # Count total RTO orders
        total_delivered_ndr_count = Orders.objects.filter(ndr_action='delivered').count()
        return Response({'total_delivered_ndr_count': total_delivered_ndr_count}, status=status.HTTP_200_OK)


# Zone wise ndr count orders
class TotalZonewiseCount(APIView):
    def get(self, request, format=None):
        # Assuming you have a 'zone' field in your Orders model
        total_counts_by_zone = (
            Orders.objects
            .values('zone')
            .annotate(
                total_ndr_count=Count(Case(When(ndr_status='y', then=Value(1)), output_field=IntegerField())),
                total_delivered_count=Count(Case(When(ndr_action='delivered', then=Value(1)), output_field=IntegerField())),
            )
            .order_by('zone')
        )
        result = [
            {
                'zone': item['zone'],
                'total_ndr_count': item['total_ndr_count'],
                'total_delivered_count': item['total_delivered_count']
            }
            for item in total_counts_by_zone
        ]
        return Response(result, status=status.HTTP_200_OK)

#count all ndr status 
class TotalAllNdrCount(APIView):
    def get(self, request, format=None):
        # Calculate the date 180 days ago from today
        one_eighty_days_ago = timezone.now() - timedelta(days=30)
        # Get weekly counts for 'ndr_status'
        ndr_status_counts = Orders.objects.filter(
            ~Q(ndr_status='n') & ~Q(ndr_status='y') & ~Q(ndr_status='in_transit') & ~Q(ndr_status='requested'),
            inserted__gte=one_eighty_days_ago
        ).annotate(
            week=TruncWeek('inserted')
        ).values('week', 'ndr_status').annotate(
            total_count=Count('id')
        ).order_by('week', 'ndr_status')
        # Get weekly counts for 'ndr_action'
        ndr_action_counts = Orders.objects.filter(
            ~Q(ndr_action='n') & ~Q(ndr_action='in_transit') & ~Q(ndr_action='requested'),
            inserted__gte=one_eighty_days_ago
        ).annotate(
            week=TruncWeek('inserted')
        ).values('week', 'ndr_action').annotate(
            total_count=Count('id')
        ).order_by('week', 'ndr_action')
        # Prepare the response data
        ndr_status_result = []
        ndr_action_result = []
        for data in ndr_status_counts:
            ndr_status_result.append({
                'week': data['week'].strftime('%U'),
                'ndr_status': data['ndr_status'],
                'total_count': data['total_count'],
            })
        for data in ndr_action_counts:
            ndr_action_result.append({
                'week': data['week'].strftime('%U'),
                'ndr_action': data['ndr_action'],
                'total_count': data['total_count'],
            })
        return Response({'ndr_status': ndr_status_result, 'ndr_action': ndr_action_result}, status=status.HTTP_200_OK)
#Api for count ndr raised and ndr deleverd
class NdrRaiseByCourierPathner(APIView):
    def get(self, request, format=None):
        # Using conditional expressions to count ndr_status='y' and ndr_action='delivered'
        ndr_counts = Orders.objects.values('courier_partner').annotate(
            total_count=Count('id'),
            ndr_raise_count=Count(Case(When(ndr_status='y', then=Value(1)), output_field='id')),
            ndr_delivered_count=Count(Case(When(ndr_action='delivered', then=Value(1)), output_field='id')),
        )
        # Filter out results where courier_partner is null and both counts are zero
        ndr_counts = ndr_counts.exclude(
            courier_partner__isnull=True,
            ndr_raise_count=0,
            ndr_delivered_count=0
        )
        # Prepare the response data
        result = [
            {
                'courier_partner': data['courier_partner'],
                'ndr_raise_count': data['ndr_raise_count'],
                'ndr_delivered_count': data['ndr_delivered_count'],
            }
            for data in ndr_counts
        ]
        return Response({'ndr_counts': result}, status=status.HTTP_200_OK)

# Api for ndr reason split count (hold because data not accordingto does not matchu)
class NdrReasonSplitCount(APIView):
    def get(self, request, format=None):
        twelve_months_ago = timezone.now() - timedelta(days=365)
        monthly_ndr_counts = Orders.objects.filter(
            ndr_status='y',
            inserted__gte=twelve_months_ago
        ).annotate(
            month=TruncMonth('inserted')
        ).values('month').annotate(
            total_count=Count('id')
        ).order_by('month')
        response_data = [
            {
                'month': data['month'].strftime('%B'),  # Month name
                'total_count': data['total_count'],
            }
            for data in monthly_ndr_counts
        ]
        return Response({'monthly_ndr_counts': response_data}, status=status.HTTP_200_OK)

class CastAsDate(Func):
    function = 'CAST'
    template = '%(function)s(%(expressions)s AS DATE)'
    output_field = DateField()

class NdrAttemptsByResponce(APIView):
    def get(self, request, format=None):
     # Calculate the date 30 days ago from today
        thirty_days_ago = timezone.now() - timedelta(days=30)

        # Get NDR attempts for each order in the last 30 days
        ndr_attempts = NdrAttemps.objects.filter(
            order_id__in=Orders.objects.filter(inserted__gte=thirty_days_ago).values_list('id', flat=True)
        ).values('raised_date', 'remark').annotate(
            total_attempts=Count('id')
        )
        response_data = []
        for data in ndr_attempts:
            raised_date = datetime.strptime(data['raised_date'], '%Y-%m-%d').date()
            week_start = raised_date - timedelta(days=raised_date.weekday())
            
            response_data.append({
                'week': week_start.strftime("%U"),  # Get ISO week number
                'remark': data['remark'],
                'total_attempts': data['total_attempts'],
            })
        return Response({'ndr_attempts_by_remark': response_data}, status=status.HTTP_200_OK)

#Api for count totaltotal no  ndr attempt 
class TotalNdrAttempts(APIView):
    def get(self, request, format=None):
        # Get total NDR attempts for each order ID
        total_ndr_attempts = NdrAttemps.objects.values('order_id').annotate(
            total_attempts=Count('id')
        )
        response_data = [
            {
                'order_id': data['order_id'],
                'total_attempts': data['total_attempts'],
            }
            for data in total_ndr_attempts
        ]
        return Response({'total_ndr_attempts': response_data}, status=status.HTTP_200_OK)

from calendar import month_name 
class NdrTotalDelevryAttempt(APIView):
     def get(self, request, format=None):
        # Calculate the date one year ago from today
        one_year_ago = datetime.now() - timedelta(days=365)
        # Get total NDR attempts with ndr_status='delivered' for each order in the last one year, grouped by month
        ndr_delivered_data = Orders.objects.filter(ndr_status='delivered', delivered_date__gte=one_year_ago).annotate(
            month=TruncMonth('delivered_date'),
            total_ndr_delivered=Count('id')
        ).values('month').annotate(
            total_ndr_delivered=Count('id')
        ).order_by('month')
        response_data = [
            {
                'month': month_name[data['month'].month],
                'total_ndr_delivered': data['total_ndr_delivered'],
            }
            for data in ndr_delivered_data
        ]
        return Response({'ndr_delivered_data': response_data}, status=status.HTTP_200_OK)



#calculate total deley order (this api not given )
class CalculateOrderDelay(APIView):
      def get(self, request, format=None):
        # Calculate the date one year ago from today
        one_year_ago = datetime.now() - timedelta(days=30)
        # Calculate the expected pickup date based on conditions
        orders_data = Orders.objects.annotate(
            expected_pickup_date=ExpressionWrapper(
                F('awb_assigned_date') + timedelta(days=1),
                output_field=DateField()
            )
        ).annotate(
            pickup_date=F('awb_assigned_date') + timedelta(days=1),
            is_delayed=ExpressionWrapper(
                Case(
                    When(
                        inserted__lt=one_year_ago,
                        then=True
                    ),
                    default=False,
                    output_field=BooleanField()
                ),
                output_field=BooleanField()
            )
        ).values(
            'expected_delivery_date',
            'pickup_date',
            'is_delayed'
        )

        response_data = []
        for order in orders_data:
            response_data.append({
                'expected_delivery_date': order['expected_delivery_date'],
                'pickup_date': order['pickup_date'],
                'is_delayed': order['is_delayed'],
            })

        return Response({'pickup_delay_data': response_data})


class MisroutedDelay(APIView):
    def get(self, request, format=None):
        miss_routed_deley= Orders.objects.filter(status='misrouted').count()
        return Response({'miss_routed_deley': miss_routed_deley}, status=status.HTTP_200_OK)

class LostDeley(APIView):
    def get(self, request, format=None):
        lost_delay = Orders.objects.filter(status='lost').count()
        return Response({'lost_delay': lost_delay}, status=status.HTTP_200_OK)


class DamageDelay(APIView):
    def get(self, request, format=None):
        damage_delay = Orders.objects.filter(status='damaged').count()
        return Response({'damage_delay': damage_delay}, status=status.HTTP_200_OK)

class DestroyedDelay(APIView):
    def get(self, request, format=None):
        destroyed_delay = Orders.objects.filter(status='destroyed').count()
        return Response({'destroyed_delay': destroyed_delay}, status=status.HTTP_200_OK)

# data does not come proper 
class ForwordDeley(APIView):
    def get(self, request, format=None):
        # Calculate the date 30 days ago from today
        thirty_days_ago = datetime.now() - timedelta(days=365)

        # Get forward delivery delay data per week
        forward_delivery_delay_data = Orders.objects.filter(
            o_type='forward',
            inserted__gte=thirty_days_ago
        ).annotate(
            month_start=TruncMonth('expected_delivery_date'),
            is_delayed=Case(
                When(
                    delivered_date__gt=F('expected_delivery_date'),
                    then=Value(False),
                ),
                default=Value(True),
                output_field=BooleanField(),
            )
        ).filter(is_delayed=True).values('month_start').annotate(
            forward_delivery_delay_count=Count('id')
        ).order_by('month_start')

        # Prepare the response data
        response_data = [
            {
                'month_start': data['month_start'].strftime("%B"),
                'forward_delivery_delay_count': data['forward_delivery_delay_count'],
            }
            for data in forward_delivery_delay_data
        ]
        return Response({'forward_delivery_delay_data': response_data})


#Api for Last Mile Deley
class LstMileDeley(APIView):
     def get(self, request, format=None):
        # Calculate the date 30 days ago from today
        thirty_days_ago = datetime.now() - timedelta(days=365)

        # Get forward delivery delay data per week
        delivery_delay_data = Orders.objects.filter(
            
            inserted__gte=thirty_days_ago,
            expected_delivery_date__isnull=False
        ).annotate(
            month_start=TruncMonth('expected_delivery_date'),
            is_delayed=Case(
                When(
                    delivered_date__gt=F('expected_delivery_date'),
                    then=Value(False),
                ),
                default=Value(True),
                output_field=BooleanField(),
            )
        ).filter(is_delayed=True).values('month_start').annotate(
            delivery_delay_count=Count('id')
        ).order_by('month_start')

        # Prepare the response data
        response_data = [
            {
                'month_start': data['month_start'].strftime("%B"),
                'delivery_delay_count': data['delivery_delay_count'],
            }
            for data in delivery_delay_data
        ]
        return Response({'delivery_delay_data': response_data})

#Api for calculate Reverce deley(condition check shuld be on inserted at)
class ReverseDeley(APIView):
    def get(self, request, format=None):
        # Calculate the date 30 days ago from today
        thirty_days_ago = datetime.now() - timedelta(days=365)
        # Get reverse delivery delay data per week
        delivery_delay_data = Orders.objects.filter(
            o_type='reverse',
            inserted__gte=thirty_days_ago,
            expected_delivery_date__isnull=False  # Filter out null values
        ).annotate(
            month_start=TruncMonth('expected_delivery_date'),
            is_delayed=Case(
                When(
                    delivered_date__gt=F('expected_delivery_date'),
                    then=Value(False),
                ),
                default=Value(True),
                output_field=BooleanField(),
            )
        ).filter(is_delayed=True).values('month_start').annotate(
            delivery_delay_count=Count('id')
        ).order_by('month_start')

        # Prepare the response data
        response_data = [
            {
                'month_start': data['month_start'].strftime("%B"),
                'delivery_delay_count': data['delivery_delay_count'],
            }
            for data in delivery_delay_data
        ]
        return Response({'delivery_delay_data': response_data})

# intrangit deley
class IntrangitDeley(APIView):
    def get(self, request, format=None):
        # Calculate the date 30 days ago from today
        thirty_days_ago = datetime.now() - timedelta(days=365)
        # Get reverse delivery delay data per week
        delivery_delay_data = Orders.objects.filter(
            status='in_transit',
            inserted__gte=thirty_days_ago,
            expected_delivery_date__isnull=False  # Filter out null values
        ).annotate(
            month_start=TruncMonth('expected_delivery_date'),
            is_delayed=Case(
                When(
                    delivered_date__gt=F('expected_delivery_date'),
                    then=Value(False),
                ),
                default=Value(True),
                output_field=BooleanField(),
            )
        ).filter(is_delayed=True).values('month_start').annotate(
            delivery_delay_count=Count('id')
        ).order_by('month_start')

        # Prepare the response data
        response_data = [
            {
                'month_start': data['month_start'].strftime("%B"),
                'delivery_delay_count': data['delivery_delay_count'],
            }
            for data in delivery_delay_data
        ]
        return Response({'delivery_delay_data': response_data})

#################### end deley section here#################

###################wait section start here#############


class WeightProfileInKg(APIView):
    def get(self, request, format=None):
        # Convert 'weight' field to a numeric type (grams to kilograms) and order by it
        weight_in_kg = Orders.objects.annotate(
            numeric_weight_kg=ExpressionWrapper(
                Cast('weight', FloatField()) / Value(1000),  # Convert grams to kilograms
                output_field=FloatField()
            )
        ).values('weight', 'numeric_weight_kg').order_by('-numeric_weight_kg')[:10]
        return Response({'weight_in_kg': weight_in_kg}, status=status.HTTP_200_OK)


# zone wise weight count
class ZonewiseCount(APIView):
    def get(self, request, format=None):
        # Calculate the date 30 days ago from today
        thirty_days_ago = timezone.now() - timedelta(days=365)

        # Assuming you have a 'zone' field in your Orders model
        total_counts_by_zone = (
            Orders.objects
            .filter(inserted__gte=thirty_days_ago)  # Filter data for the last 30 days
            .values('zone')
            .annotate(
                total_delivered_count=Count(Case(When(status='delivered', then=Value(1)), output_field=IntegerField())),
            )
            .exclude(zone=None, total_delivered_count=0)  # Exclude entries with zone as null and count as 0
            .order_by('zone')
        )
        result = [
            {
                'zone': item['zone'],
                'total_delivered_count': item['total_delivered_count']
            }
            for item in total_counts_by_zone
        ]
        return Response(result, status=status.HTTP_200_OK)

#Api for Ofd avrage data
class OfdData(APIView):
    def get(self, request, format=None):
        # Calculate the date 30 days ago from today
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)

        # Get total counts for each month in the last 30 days
        monthly_counts = Orders.objects.filter(
            inserted__gte=thirty_days_ago
        ).annotate(
            month_start=TruncMonth('inserted')
        ).values('month_start').annotate(
            total_orders=Count('id'),
            oft_transit_data=Count('id', filter=Q(status='transit')),
            oft_delivered_data=Count('id', filter=Q(status='delivered'))
        ).order_by('month_start')

        # Format the response data for each month
        response_data = [
            {
                'month_start': item['month_start'].strftime("%B"),
                'average_transit': item['oft_transit_data'] / item['total_orders'] if item['total_orders'] > 0 else 0,
                'average_delivered': item['oft_delivered_data'] / item['total_orders'] if item['total_orders'] > 0 else 0,
            }
            for item in monthly_counts
        ]

        return Response(response_data, status=status.HTTP_200_OK)