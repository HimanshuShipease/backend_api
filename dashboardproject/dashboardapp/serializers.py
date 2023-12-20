from rest_framework import serializers
from django.db import models
from dashboardapp.models import Parentsidebar,OrderTracking,Orders

class PsidebarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parentsidebar
        fields = ['id', 'p_name']


class OrderTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTracking
        fields = '__all__'

class ChannelWiseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

############ ndr section start here#########
class ZoneWiseNdrOrdersSerializer(serializers.Serializer):
    zone = models.CharField(max_length=100)
    ndr_status = models.CharField(max_length=1)



############# shipment deley###############

class lostShipmentDeleySerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields =['status']

############### overview section start here###############

class LastthirtyDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields =['status',
        'order_number',
        'customer_order_number',
        'awb_number',
        'courier_partner',
        'shipping_charges',
        'total_charges',
        'total_charges',
        'weight',
        'status'
        ]
