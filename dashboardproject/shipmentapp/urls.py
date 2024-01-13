from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shipmentapp import views
 
urlpatterns = [ 
    path('ndrrasedorder/', views.NdrRaisedApi.as_view(), name='ndrrasedorder'),
    path('actionrequestedshipment/', views.ActionRequestedApi.as_view(), name='actionrequestedshipment'),
    path('actionreqshipment/', views.ActionReqApi.as_view(), name='actionreqshipment'),
    path('deleverdshipment/', views.Deleverdndrapi.as_view(), name='deleverdshipment'),
    path('ndrshipment/', views.Rtoshipmentapi.as_view(), name='ndrshipment'),
    path('ndrshipment-org/', views.ActionRequestedApi_ogg.as_view(), name='ndrshipment-org')
]

urlpatterns = format_suffix_patterns(urlpatterns)
