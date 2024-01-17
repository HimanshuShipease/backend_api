from django.db import models


class Sellers(models.Model):
    code = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    onhold_balance = models.CharField(max_length=10, blank=True, null=True)
    cod_balance = models.FloatField(blank=True, null=True)
    last_remitted = models.CharField(max_length=10, blank=True, null=True)
    basic_information = models.CharField(max_length=1, blank=True, null=True)
    account_information = models.CharField(max_length=1, blank=True, null=True)
    kyc_information = models.CharField(max_length=1, blank=True, null=True)
    agreement_information = models.CharField(max_length=1, blank=True, null=True)
    warehouse_status = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    registered_ip = models.CharField(max_length=20)
    status = models.CharField(max_length=1)
    verified = models.CharField(max_length=1)
    created_by = models.CharField(max_length=20)
    google_id = models.TextField(blank=True, null=True)
    profile_image = models.TextField(blank=True, null=True)
    plan_id = models.IntegerField(blank=True, null=True)
    gst_certificate_status = models.CharField(max_length=1, blank=True, null=True)
    cheque_status = models.CharField(max_length=1, blank=True, null=True)
    document_status = models.CharField(max_length=1, blank=True, null=True)
    agreement_status = models.CharField(max_length=1, blank=True, null=True)
    rto_charge = models.CharField(max_length=4, blank=True, null=True)
    early_cod_charge = models.FloatField(blank=True, null=True)
    reconciliation_days = models.IntegerField(blank=True, null=True)
    courier_priority_1 = models.CharField(max_length=50, blank=True, null=True)
    courier_priority_2 = models.CharField(max_length=50, blank=True, null=True)
    courier_priority_3 = models.CharField(max_length=50, blank=True, null=True)
    courier_priority_4 = models.CharField(max_length=50, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    permission = models.CharField(max_length=10, blank=True, null=True)
    api_key = models.CharField(max_length=60, blank=True, null=True)
    reverse_charge = models.IntegerField(blank=True, null=True)
    full_label_display = models.CharField(max_length=1, blank=True, null=True)
    sms_service = models.CharField(max_length=1, blank=True, null=True)
    pincode_editable = models.CharField(max_length=1, blank=True, null=True)
    essentials = models.CharField(max_length=1, blank=True, null=True)
    easyecom_token = models.CharField(max_length=150, blank=True, null=True)
    display_invoice = models.CharField(max_length=1)
    remmitance_days = models.IntegerField()
    sku_mapping = models.CharField(max_length=10, blank=True, null=True)
    order_number_prefix = models.CharField(max_length=25, blank=True, null=True)
    sequence_generator = models.CharField(max_length=1, blank=True, null=True)
    sequence_prefix = models.CharField(max_length=25, blank=True, null=True)
    sequence_start_value = models.BigIntegerField(blank=True, null=True)
    sequence_current_value = models.BigIntegerField(blank=True, null=True)
    zone_type = models.CharField(max_length=8)
    xb_type = models.CharField(max_length=25, blank=True, null=True)
    seller_order_type = models.CharField(max_length=3)
    seller_order_type_updated_at = models.DateTimeField(blank=True, null=True)
    zone_type_updated_at = models.DateTimeField(blank=True, null=True)
    employee_flag_enabled = models.CharField(max_length=1, blank=True, null=True)
    has_custom_credentials = models.CharField(max_length=1)
    webhook_enabled = models.CharField(max_length=1)
    webhook_url = models.TextField(blank=True, null=True)
    webhook_api_key = models.CharField(max_length=100, blank=True, null=True)
    iec_code = models.CharField(max_length=50, blank=True, null=True)
    ad_code = models.CharField(max_length=50, blank=True, null=True)
    is_alpha = models.CharField(max_length=3, blank=True, null=True)
    is_international = models.CharField(max_length=1)
    onboarded_by = models.IntegerField(blank=True, null=True)
    auto_manifest_enabled = models.CharField(max_length=1)
    cheapest_enabled = models.CharField(max_length=1)
    product_name_as_sku = models.CharField(max_length=1)
    brand_tracking_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sellers'


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



class Invoice(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    inv_id = models.CharField(max_length=50, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    total = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    gst_amount = models.FloatField(blank=True, null=True)
    invoice_amount = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=1)
    invoice_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice'


class InvoiceOrders(models.Model):
    invoice_id = models.IntegerField()
    order_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_orders'


class BillReceipt(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    note_number = models.CharField(max_length=50, blank=True, null=True)
    total = models.CharField(max_length=10, blank=True, null=True)
    note_date = models.DateTimeField(blank=True, null=True)
    note_reason = models.CharField(max_length=50, blank=True, null=True)
    gstin = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_receipt'
