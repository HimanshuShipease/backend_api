from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from billing_app import views
# CreditReceptLog
urlpatterns = [
    path('shiping-charges/', views.ShipingChargesApi.as_view(), name='shiping-charges'),
    path('remitancelog/', views.RemitenceLog.as_view(), name='remitancelog'),
    path('rechargelog/', views.RechargeLogs.as_view(), name='rechargelog'),
    path('invoicelog/', views.InvoiceLog.as_view(), name='invoicelog'),
    path('passbooklog/', views.PassbookLog.as_view(), name='passbooklog'),
    path('creditreceptlog/', views.CreditReceptLog.as_view(), name='creditreceptlog')

]