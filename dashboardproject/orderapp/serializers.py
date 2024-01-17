from rest_framework import serializers
from django.db import models
from dashboardapp.models import Parentsidebar,OrderTracking,Orders


class CreateOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields=['id',
                'customer_order_number',
                'o_type','order_type',
                'shipment_type',
                'number_of_packets',
                'number_of_packets',
                's_customer_name',
                's_contact',
                's_address_line1',
                's_address_line2',
                's_pincode',
                's_country',
                's_state',
                's_city',
                'product_sku',
                'product_name',
                'product_qty',
                'weight',
                'length',
                'breadth',
                'height',
                'invoice_amount',
                'shipping_charges',
                'cod_charges',
                'discount',
                'reseller_name',
                'p_warehouse_name',
                'vol_weight',
                'inserted',

                ]     
