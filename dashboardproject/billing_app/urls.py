from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from billing_app import views
# 
urlpatterns = [
    path('shiping-charges/', views.ShipingChargesApi.as_view(), name='shiping-charges'),
     path('remitancelog/', views.RemitenceLog.as_view(), name='remitancelog'),
    path('rechargelog/', views.RechargeLogs.as_view(), name='rechargelog')
]