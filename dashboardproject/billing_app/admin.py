from django.contrib import admin
from billing_app.models import Transactions,CodTransactions

# Register your models here.
admin.site.register(Transactions)
admin.site.register(CodTransactions)