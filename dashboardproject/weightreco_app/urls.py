from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from weightreco_app import views
# WeightReconciliationList_ogg
urlpatterns = [
    path('weight-recancel/', views.WeightReconciliationList.as_view(), name='weight-recancel'),
    path('weight-recancel-data/', views.WeightReconciliationList_org.as_view(), name='weight-recancel-data'),
   
]