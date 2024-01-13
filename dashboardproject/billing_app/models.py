from django.db import models



class Transactions(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    balance = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    redeem_type = models.CharField(max_length=1, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    razorpay_payment_id = models.TextField(blank=True, null=True)
    razorpay_order_id = models.TextField(blank=True, null=True)
    razorpay_signature = models.TextField(blank=True, null=True)
    method = models.CharField(max_length=30, blank=True, null=True)
    utr_number = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class CodTransactions(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    crf_id = models.CharField(max_length=10, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    redeem_type = models.CharField(max_length=1, blank=True, null=True)
    utr_number = models.CharField(max_length=30, blank=True, null=True)
    early_cod_charge = models.IntegerField(blank=True, null=True)
    pay_type = models.CharField(max_length=10, blank=True, null=True)
    remitted_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cod_transactions'        