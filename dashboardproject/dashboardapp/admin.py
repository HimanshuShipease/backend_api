from django.contrib import admin
# from dashboardapp.models import Parentsidebar,OrderTracking,Orders,NdrAttemps

from .models import Parentsidebar,OrderTracking,Orders,NdrAttemps,Products


admin.site.register(Parentsidebar)
# admin.site.register(OrderTracking)
@admin.register(OrderTracking)
class OrderTrackingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderTracking._meta.get_fields()]
admin.site.register(Orders)

admin.site.register(NdrAttemps)
admin.site.register(Products)
