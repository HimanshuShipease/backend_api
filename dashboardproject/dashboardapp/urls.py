from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from dashboardapp import views
# 
urlpatterns = [
    ########### start Api for order dashboard########
    path('p-sidebar/', views.Psidebarlist.as_view()),
    path('totalorder/', views.Totalorderscount.as_view()),
    path('totalcancelorder/', views.TotalCancelOrderCount.as_view()),
    path('totaldeleverdorder/', views.TotalDeleverdOrderCount.as_view()),
    path('totalrtoordercount/', views.TotalReturnToOriginOrderCount.as_view()),
    path('monthly-orders/', views.MonthlyOrders.as_view()),
    path('cancel-orders-graph/', views.TotalCancelOrderGraph.as_view()),
    path('channal-wise-order/', views.ChannalWiseGraph.as_view()),
    path('state-wise-order/', views.StateWiseData.as_view()),
    path('weekly-wise-order/', views.CountOrderType.as_view()),
    path('top-product-sku/', views.TopProductSKU.as_view(), name='top-product-sku'),
    path('sks-mps-product/', views.PopularSKUs.as_view(), name='sks-mps-product'),

    ########### end Api for order dashboard ######## TopRTOPCouriarPathner
    path('calculate-status-wise-rto/', views.CalculateRto.as_view(), name='calculate-status-wise-rto'),
    path('trangit-intrangitdata/', views.InTransitAndTransit.as_view(), name='trangit-intrangitdata'),
    path('top-rto-city/', views.TopRTOCity.as_view(), name='top-rto-city'),
    path('top-rto-pincode/', views.TopRTOPinCode.as_view(), name='top-rto-pincode'),
    path('year-wise-rto-count/', views.MonthlyRTOOrders.as_view(), name='year-wise-rto-count'),
    path('top-rto-courier/', views.TopRTOPCouriarPathner.as_view(), name='top-rto-courier'),

    #### end api for rto section here   ################
    ##### start NDR section here ############# CalculateOrderDelay
    path('total-ndr/', views.CalculateTotalNdr.as_view(), name='total-ndr'),
    path('total-required-ndr/', views.CalculateTotalNdr.as_view(), name='total-required-ndr'),
    path('total-requested-ndr/', views.CalculateTotalNdr.as_view(), name='total-requested-ndr'),             
    path('total-deleverd-ndr/', views.TotalDeleverdNdr.as_view(), name='total-deleverd-ndr'),
    path('total-zone-wise-ndr/', views.TotalZonewiseCount.as_view(), name='total-zone-wise-ndr'),
    path('total-ndr-count/', views.TotalAllNdrCount.as_view(), name='total-ndr-count'),
    path('ndr-courierpathner-count/', views.NdrRaiseByCourierPathner.as_view(), name='ndr-courierpathner-count'),
    path('ndr-reason-split/', views.NdrReasonSplitCount.as_view(), name='ndr-reason-split'),
    path('ndr-responce-count/', views.NdrAttemptsByResponce.as_view(), name='ndr-responce-count'),
    path('total-ndr-attempt/', views.TotalNdrAttempts.as_view(), name='total-ndr-attempt'),
    path('total-ndr-delevery-attempt/', views.NdrTotalDelevryAttempt.as_view(), name='total-ndr-delevery-attempt/'),

    ##### end NDR section here ############# CalculateOrderDelay

    ##### Start deley section here ############# IntrangitDeley

    path('pending-deley-order/', views.CalculateOrderDelay.as_view(), name='pending-deley-order/'),
    path('misrouted-deley/', views.MisroutedDelay.as_view(), name='misrouted-deley/'),
    path('lost-deley/', views.LostDeley.as_view(), name='lost-deley/'),
    path('damage-deley/', views.DamageDelay.as_view(), name='damage-deley/'),
    path('destroyed-deley/', views.DestroyedDelay.as_view(), name='destroyed-deley/'),
    path('forword-deley/', views.ForwordDeley.as_view(), name='forword-deley/'),
    path('last-mile-deley/', views.LstMileDeley.as_view(), name='last-mile-deley/'),
    path('reverse-deley/', views.ReverseDeley.as_view(), name='reverse-deley'),
    path('intrangit-deley/', views.IntrangitDeley.as_view(), name='intrangit-deley/'),

    #################weight section start here########### ShipmentOverviewByCourier

    path('top-weight/', views.WeightProfileInKg.as_view(), name='top-weight/'),
    path('zone-wise-data/', views.ZonewiseCount.as_view(), name='zone-wise-dat/'),
    path('ofd-data/', views.OfdData.as_view(), name='ofd-dat/'),
    path('shipment-overview/', views.ShipmentOverviewByCourier.as_view(), name='shipment-overview/'),

    ################# overview section start here ###########################  SixMonthRvenuAnalist

    path('status-wise-graph/', views.StatusWiseGraph.as_view(), name='status-wise-graph'),
    path('top-customer/', views.CalculateBestCustomer.as_view(), name='top-customer'),
    path('avg-sellingprice/', views.AvrageSellingPrice.as_view(), name='avg-sellingprice'),
    path('daly-shipment/', views.DailyShipment.as_view(), name='daly-shipment'),
    path('today-revenue/', views.TodayRevenueCount.as_view(), name='today-revenue'),
    path('daily-prefrences/', views.DailyPrefrence.as_view(), name='daily-prefrences'),
    path('late-delevery-prefrence/', views.LateDeleveryPrefrence.as_view(), name='late-delevery-prefrence'),
    path('lastthirtydata/', views.LastThirtyDayData.as_view(), name='lastthirtydata'),
    path('top-couriar-pathner/', views.TopCouriarPathner.as_view(), name='top-couriar-pathner'),
    path('top-customer-count/', views.TopCustomerApi.as_view(), name='top-customer-count'),
    path('ndr-detail/', views.NdrDetail.as_view(), name='ndr-detail'),
    path('topproduct/', views.TopProduct.as_view(), name='topproduct'),
    path('statewiseproduct/', views.TopProductStateWise.as_view(), name='statewiseproduct'),
    path('orderplaced/', views.OrderPlaced.as_view(), name='orderplaced'),
    path('waitdipute/', views.WeightDisputed.as_view(), name='waitdipute'),
    path('one-day-revenue/', views.OneRvenuAnalist.as_view(), name='one-day-revenue'),
    path('one-week-revenue/', views.OneWeekRvenuAnalist.as_view(), name='one-week-revenue'),
    path('one-month-revenue/', views.OneMonthRvenuAnalist.as_view(), name='one-month-revenue'),
    path('three-month-revenue/', views.ThreeMonthRvenuAnalist.as_view(), name='three-month-revenue'),
    path('six-month-revenue/', views.SixMonthRvenuAnalist.as_view(), name='six-month-revenue'),
    path('one-year-revenue/', views.OneYearRevenueAnalist.as_view(), name='one-year-revenue'),
    






    

]
