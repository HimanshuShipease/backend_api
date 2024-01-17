from rest_framework import serializers
from django.db import models
from weightreco_app.models import WeightReconciliation,WeightReconciliationHistory,Partners
from dashboardapp.models import Orders


class WeightReconciliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightReconciliation
        fields = '__all__'



# class NdrAttemptsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NdrAttemps
#         fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'   
        
        

# class CombinedSerializer(serializers.Serializer):
#     order_id = serializers.IntegerField(source='id')
#     customer_order_number = serializers.CharField()
#     s_customer_name = serializers.CharField()
#     ndr_raised_time = serializers.CharField()
#     s_contact_code = serializers.CharField()
#     weight = serializers.CharField()
#     length = serializers.CharField()
#     breadth = serializers.CharField()
#     height = serializers.CharField()
#     awb_number = serializers.CharField()
#     product_name = serializers.CharField()
#     ndr_attempts_data = serializers.ListField(child=WeightReconciliationSerializer(), read_only=True)
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         ndr_attempts_data = WeightReconciliationSerializer(instance, many=True).data
#         representation.update({'ndr_attempts_data': ndr_attempts_data})

#         return representation
    


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['order_number', 'awb_number','seller_id','courier_partner','product_name' ]


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ['id', 'keyword','image' ]

class WeightReconciliationSerializer(serializers.ModelSerializer):
    order = OrdersSerializer(read_only=True)

    class Meta:
        model = WeightReconciliation
        fields = ['id', 
                  'created',
                  'seller_id',
                  'awb_number',
                  'e_weight',
                  'e_length',
                  'e_breadth', 
                  'e_height',
                  'applied_amount',
                  'c_weight', 
                  'c_length', 
                  'c_breadth', 
                  'c_height', 
                  'charged_amount', 
                  's_weight', 
                  's_length', 
                  's_breadth',
                  's_height', 
                  'settled_amount', 
                  'remark' ,
                  'created', 
                  'action_taken_by', 
                  'status', 
                  'display_status', 
                  'is_error', 
                  'error_message', 
                  'uploaded_at', 
                  'order']  