from rest_framework import serializers
from django.db import models
from dashboardapp.models import Parentsidebar,OrderTracking,Orders


class CreateOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields='__all__'        
