# from rest_framework import serializers
# from django.db import models
# from dashboardapp.models import OrderTracking,Orders,NdrAttemps


      
# class ActionRequestedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Orders
#         fields = '__all__'


# class NdrSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NdrAttemps
#         fields = '__all__'        



from rest_framework import serializers
from django.db import models
from dashboardapp.models import OrderTracking,Orders,NdrAttemps


class NdrAttemptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NdrAttemps
        fields = '__all__'

class ActionRequestedSerializer(serializers.ModelSerializer):
    # ndr_attempts = NdrAttemptsSerializer(many=True, read_only=True)

    class Meta:
        model = Orders
        fields = '__all__'   
        
        

class CombinedSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(source='id')
    customer_order_number = serializers.CharField()
    s_customer_name= serializers.CharField()
    ndr_raised_time=serializers.CharField()
    s_contact_code=serializers.CharField()
    weight=serializers.CharField()
    length=serializers.CharField()
    breadth=serializers.CharField()
    height=serializers.CharField()
    awb_number=serializers.CharField()
    product_name=serializers.CharField()
    
    # Add other fields from the Orders model that you want to include
    ndr_attempts_data = serializers.ListField(child=serializers.DictField(), read_only=True)
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        ndr_attempts_data = representation.pop('ndr_attempts_data', [])
        representation.update({'ndr_attempts_data': ndr_attempts_data})

        return representation