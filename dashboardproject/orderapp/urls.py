from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from orderapp import views
 
urlpatterns = [ 
    path('allorderdetail/', views.FetchAllOrdersDetail.as_view(), name='allorderdetail'),
    path('allorderdetailid/<int:pk>/', views.FetchAllOrdersDetailById.as_view(), name='allorderdetailid'),
    path('unprocessable/', views.UnprocessableOrder.as_view(), name='unprocessable'),
    path('processableorder/', views.ProcessableOrder.as_view(), name='processableorder'),
    path('pickedallorders/', views.ReadyToShipOrder.as_view(), name='pickedallorders'),
    path('returnallorder/', views.ReturnOrder.as_view(), name='returnallorder'),
    path('createorder/', views.CreateOrderapi.as_view(), name='createorder'),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)
