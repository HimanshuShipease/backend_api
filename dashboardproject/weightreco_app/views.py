from django.shortcuts import render



from weightreco_app.models import WeightReconciliation,Partners
from weightreco_app.serializers import WeightReconciliationSerializer,OrdersSerializer,PartnersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import datetime, timedelta
from dashboardapp.models import Orders

global_seller_id=14366

class WeightReconciliationList(APIView):
    def get(self, request, format=None):
        one_month_ago = datetime.now() - timedelta(days=30)
        snippets = WeightReconciliation.objects.all()[:30]
        serializer = WeightReconciliationSerializer(snippets, many=True)
        return Response(serializer.data)
    



class WeightReconciliationList_org(APIView):
    def get(self, request, format=None):
        global_seller_id = 14366
        set_date = timezone.now() - timedelta(days=80)

        # Get the last 30 WeightReconciliation objects
        last_30_reconciliations = WeightReconciliation.objects.order_by('-created')[:30]

        # Extract awb_number values from the last 30 reconciliations
        order_numbers = [reconciliation.awb_number for reconciliation in last_30_reconciliations]

        # Fetch the last 30 order details from Orders for the specified order numbers
        orders = Orders.objects.filter(awb_number__in=order_numbers).order_by('-inserted')[:30]

        # Serialize the data
        order_serializer = OrdersSerializer(orders, many=True)
        reconciliation_serializer = WeightReconciliationSerializer(last_30_reconciliations, many=True)

        # Combine the serialized data only when both awb_numbers match
        combined_data = []
        for order_data in order_serializer.data:
            # Find the corresponding reconciliation details
            reconciliation_data = next((r for r in reconciliation_serializer.data if r['awb_number'] == order_data['awb_number']), None)
            if reconciliation_data:
                # Find partner information based on courier_partner from Orders and keyword_name from Partners
                courier_partner = order_data.get('courier_partner')
                partner = Partners.objects.filter(keyword=courier_partner).first()

                combined_data.append({
                    'order_details': order_data,
                    'reconciliation_details': reconciliation_data,
                    'partner_details': PartnersSerializer(partner).data if partner else None
                })

        return Response(combined_data)
        
