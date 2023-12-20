# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountInformations(models.Model):
    seller_id = models.IntegerField()
    account_holder_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=100, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    ifsc_code = models.CharField(max_length=15, blank=True, null=True)
    bank_branch = models.CharField(max_length=100, blank=True, null=True)
    cheque_image = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_informations'


class Admin(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    email = models.CharField(max_length=60)
    mobile = models.CharField(max_length=15)
    image = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=50)
    inserted = models.DateTimeField()
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    ins = models.CharField(max_length=1)
    del_field = models.CharField(db_column='del', max_length=1)  # Field renamed because it was a Python reserved word.
    modi = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'admin'
        
class AdminEmployee(models.Model):
    admin_id = models.IntegerField()
    name = models.CharField(max_length=100, db_collation='utf8_unicode_ci', blank=True, null=True)
    email = models.CharField(max_length=100, db_collation='utf8_unicode_ci', blank=True, null=True)
    mobile = models.CharField(max_length=20, db_collation='utf8_unicode_ci', blank=True, null=True)
    password = models.CharField(max_length=100, db_collation='utf8_unicode_ci', blank=True, null=True)
    image = models.TextField(db_collation='utf8_unicode_ci', blank=True, null=True)
    seller_ids = models.TextField(db_collation='utf8_unicode_ci', blank=True, null=True)
    status = models.CharField(max_length=10, db_collation='utf8_unicode_ci', blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_employee'


class AdminRights(models.Model):
    admin_id = models.IntegerField()
    master_id = models.IntegerField()
    ins = models.CharField(max_length=1)
    del_field = models.CharField(db_column='del', max_length=1)  # Field renamed because it was a Python reserved word.
    modi = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'admin_rights'


class AgreementInformations(models.Model):
    seller_id = models.IntegerField()
    document_upload = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_informations'


class AmazonAccessTokens(models.Model):
    refresh_token = models.TextField(blank=True, null=True)
    access_token = models.TextField(blank=True, null=True)
    generated_time = models.DateTimeField(blank=True, null=True)
    valid_till = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amazon_access_tokens'


class AramexRates(models.Model):
    weight = models.IntegerField(blank=True, null=True)
    rate_1 = models.IntegerField(blank=True, null=True)
    rate_2 = models.IntegerField(blank=True, null=True)
    rate_3 = models.IntegerField(blank=True, null=True)
    rate_4 = models.IntegerField(blank=True, null=True)
    rate_5 = models.IntegerField(blank=True, null=True)
    rate_6 = models.IntegerField(blank=True, null=True)
    rate_7 = models.IntegerField(blank=True, null=True)
    rate_8 = models.IntegerField(blank=True, null=True)
    rate_9 = models.IntegerField(blank=True, null=True)
    rate_10 = models.IntegerField(blank=True, null=True)
    rate_11 = models.IntegerField(blank=True, null=True)
    rate_12 = models.IntegerField(blank=True, null=True)
    rate_13 = models.IntegerField(blank=True, null=True)
    is_additional = models.CharField(max_length=1)
    initial_weight = models.IntegerField()
    extra_charge_1 = models.IntegerField(blank=True, null=True)
    extra_charge_2 = models.IntegerField(blank=True, null=True)
    extra_charge_3 = models.IntegerField(blank=True, null=True)
    extra_charge_4 = models.IntegerField(blank=True, null=True)
    extra_charge_5 = models.IntegerField(blank=True, null=True)
    extra_charge_6 = models.IntegerField(blank=True, null=True)
    extra_charge_7 = models.IntegerField(blank=True, null=True)
    extra_charge_8 = models.IntegerField(blank=True, null=True)
    extra_charge_9 = models.IntegerField(blank=True, null=True)
    extra_charge_10 = models.IntegerField(blank=True, null=True)
    extra_charge_11 = models.IntegerField(blank=True, null=True)
    extra_charge_12 = models.IntegerField(blank=True, null=True)
    extra_charge_13 = models.IntegerField(blank=True, null=True)
    extra_limit = models.IntegerField()
    seller_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'aramex_rates'


class AssociateInformation(models.Model):
    image = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    contents = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'associate_information'


class BasicInformations(models.Model):
    seller_id = models.IntegerField()
    company_name = models.CharField(max_length=100, blank=True, null=True)
    website_url = models.CharField(max_length=200, blank=True, null=True)
    company_logo = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    gst_certificate = models.TextField(blank=True, null=True)
    pan_number = models.CharField(max_length=15, blank=True, null=True)
    gst_number = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basic_informations'


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


class Blog(models.Model):
    image = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    by_name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog'


class BluedartDetails(models.Model):
    order_id = models.IntegerField()
    pickup_token_number = models.CharField(max_length=100, blank=True, null=True)
    shipment_pickup_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bluedart_details'


class BombaxAwbs(models.Model):
    courier_partner = models.CharField(max_length=50)
    awb_number = models.CharField(max_length=30)
    used = models.CharField(max_length=1)
    used_by = models.IntegerField(blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bombax_awbs'


class BrandTracking(models.Model):
    brand_logo = models.TextField(blank=True, null=True)
    banner1 = models.TextField(blank=True, null=True)
    banner2 = models.TextField(blank=True, null=True)
    offer_title = models.TextField(blank=True, null=True)
    product_image1 = models.TextField(blank=True, null=True)
    product_image2 = models.TextField(blank=True, null=True)
    product_image3 = models.TextField(blank=True, null=True)
    product_image4 = models.TextField(blank=True, null=True)
    product_back_image1 = models.TextField(blank=True, null=True)
    product_back_image2 = models.TextField(blank=True, null=True)
    product_back_image3 = models.TextField(blank=True, null=True)
    product_back_image4 = models.TextField(blank=True, null=True)
    product_title1 = models.CharField(max_length=100, blank=True, null=True)
    product_title2 = models.CharField(max_length=100, blank=True, null=True)
    product_title3 = models.CharField(max_length=100, blank=True, null=True)
    product_title4 = models.CharField(max_length=100, blank=True, null=True)
    product_amount1 = models.CharField(max_length=50, blank=True, null=True)
    product_amount2 = models.CharField(max_length=50, blank=True, null=True)
    product_amount3 = models.CharField(max_length=50, blank=True, null=True)
    product_amount4 = models.CharField(max_length=50, blank=True, null=True)
    seller_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brand_tracking'


class Brands(models.Model):
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'brands'


class ChannelOrdersLog(models.Model):
    channel = models.CharField(max_length=30, blank=True, null=True)
    channel_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    order_response = models.TextField(blank=True, null=True)
    item_fetched = models.CharField(max_length=1, blank=True, null=True)
    item_response = models.TextField(blank=True, null=True)
    address_fetched = models.CharField(max_length=1, blank=True, null=True)
    address_response = models.TextField(blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'channel_orders_log'


class ChannelPartners(models.Model):
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'channel_partners'


class Channels(models.Model):
    seller_id = models.IntegerField()
    channel_name = models.CharField(max_length=100, blank=True, null=True)
    channel = models.CharField(max_length=100, blank=True, null=True)
    api_key = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    store_url = models.TextField(blank=True, null=True)
    shared_secret = models.TextField(blank=True, null=True)
    woo_consumer_key = models.TextField(blank=True, null=True)
    woo_consumer_secret = models.TextField(blank=True, null=True)
    magento_access_token = models.TextField(blank=True, null=True)
    store_hippo_access_key = models.TextField(blank=True, null=True)
    kart_rocket_api_key = models.TextField(blank=True, null=True)
    auto_fulfill = models.CharField(max_length=1, blank=True, null=True)
    auto_cancel = models.CharField(max_length=1, blank=True, null=True)
    auto_cod_paid = models.CharField(max_length=1, blank=True, null=True)
    last_sync = models.DateTimeField(blank=True, null=True)
    last_id = models.CharField(max_length=20, blank=True, null=True)
    amazon_mws_token = models.CharField(max_length=200, blank=True, null=True)
    amazon_seller_id = models.CharField(max_length=200, blank=True, null=True)
    company_id = models.CharField(max_length=100, blank=True, null=True)
    company_token = models.CharField(max_length=100, blank=True, null=True)
    amazon_token = models.TextField(blank=True, null=True)
    company_carrier_id = models.CharField(max_length=50, blank=True, null=True)
    last_executed = models.DateTimeField(blank=True, null=True)
    amazon_refresh_token = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    amazon_report_id = models.TextField(blank=True, null=True)
    fetch_woocommerce_order_number = models.CharField(max_length=1)
    scince_abandon_id = models.CharField(max_length=255, blank=True, null=True)
    send_abandon_sms = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'channels'


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


class CommentsAttachment(models.Model):
    ticket_comment_id = models.IntegerField(blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments_attachment'


class Configuration(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    meta_keyword = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    favicon = models.TextField(blank=True, null=True)
    copyright = models.CharField(max_length=100, blank=True, null=True)
    minimum_balance = models.IntegerField(blank=True, null=True)
    analytics_code = models.TextField(blank=True, null=True)
    login_message = models.CharField(max_length=200, blank=True, null=True)
    register_message = models.CharField(max_length=200, blank=True, null=True)
    forget_message = models.CharField(max_length=200, blank=True, null=True)
    working_hour = models.CharField(max_length=60, blank=True, null=True)
    logistic_partner = models.CharField(max_length=1)
    channel_partner = models.CharField(max_length=1)
    brands = models.CharField(max_length=1)
    press_coverage = models.CharField(max_length=1)
    testimonial_image = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    agreement = models.TextField(blank=True, null=True)
    account_details = models.TextField(blank=True, null=True)
    stats_title = models.CharField(max_length=100, blank=True, null=True)
    associates_title = models.CharField(max_length=100, blank=True, null=True)
    steps_title = models.CharField(max_length=100, blank=True, null=True)
    signup_title = models.CharField(max_length=100, blank=True, null=True)
    ease_title = models.CharField(max_length=100, blank=True, null=True)
    logistics_title = models.CharField(max_length=100, blank=True, null=True)
    brand_title = models.CharField(max_length=100, blank=True, null=True)
    press_title = models.CharField(max_length=100, blank=True, null=True)
    channel_title = models.CharField(max_length=100, blank=True, null=True)
    subscribe_title = models.CharField(max_length=100, blank=True, null=True)
    e_cod_title = models.TextField(blank=True, null=True)
    e_cod_features = models.TextField(blank=True, null=True)
    rto_charge = models.CharField(max_length=10, blank=True, null=True)
    reconciliation_days = models.CharField(max_length=10, blank=True, null=True)
    account_holder = models.CharField(max_length=50, blank=True, null=True)
    account_number = models.CharField(max_length=30, blank=True, null=True)
    ifsc_code = models.CharField(max_length=50, blank=True, null=True)
    bank_branch = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=30, blank=True, null=True)
    gstin = models.CharField(max_length=50, blank=True, null=True)
    pan_number = models.CharField(max_length=50, blank=True, null=True)
    cin_number = models.CharField(max_length=50, blank=True, null=True)
    irn_number = models.CharField(max_length=50, blank=True, null=True)
    signature_image = models.TextField(blank=True, null=True)
    gst_percent = models.FloatField()
    invoice_generate_days = models.IntegerField(blank=True, null=True)
    hsn_number = models.CharField(max_length=50, blank=True, null=True)
    sac_number = models.CharField(max_length=50, blank=True, null=True)
    razorpay_key = models.TextField()
    razorpay_secret = models.TextField()
    reverse_charge = models.IntegerField(blank=True, null=True)
    payment_qrcode = models.TextField(blank=True, null=True)
    read_from_cache = models.CharField(max_length=10, blank=True, null=True)
    check_courier_blocking = models.CharField(max_length=10, blank=True, null=True)
    ekart_awb = models.BigIntegerField()
    last_report_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'configuration'


class Countries(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    phone_code = models.CharField(max_length=5, blank=True, null=True)
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'countries'


class CourierBlocking(models.Model):
    seller_id = models.IntegerField()
    courier_partner_id = models.IntegerField()
    is_blocked = models.CharField(max_length=10, blank=True, null=True)
    zone_a = models.CharField(max_length=10, blank=True, null=True)
    zone_b = models.CharField(max_length=10, blank=True, null=True)
    zone_c = models.CharField(max_length=10, blank=True, null=True)
    zone_d = models.CharField(max_length=10, blank=True, null=True)
    zone_e = models.CharField(max_length=10, blank=True, null=True)
    cod = models.CharField(max_length=10, blank=True, null=True)
    prepaid = models.CharField(max_length=10, blank=True, null=True)
    is_approved = models.CharField(max_length=10, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courier_blocking'


class CourierCodRemittance(models.Model):
    order_id = models.IntegerField()
    seller_id = models.IntegerField()
    customer_order_number = models.CharField(max_length=255)
    awb_number = models.CharField(max_length=255)
    courier_partner = models.CharField(max_length=255)
    awb_assigned_date = models.DateTimeField(blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    due_date_of_remittance = models.DateTimeField(blank=True, null=True)
    actual_date_of_remittance = models.DateTimeField(blank=True, null=True)
    invoice_date = models.DateTimeField(blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_reference_no = models.CharField(max_length=255, blank=True, null=True)
    transaction_mode = models.CharField(max_length=255, blank=True, null=True)
    cod_amount = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courier_cod_remittance'


class CourierCodRemittanceLog(models.Model):
    job_id = models.IntegerField()
    order_id = models.IntegerField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    customer_order_number = models.CharField(max_length=255, blank=True, null=True)
    awb_number = models.CharField(max_length=255, blank=True, null=True)
    courier_partner = models.CharField(max_length=255, blank=True, null=True)
    awb_assigned_date = models.DateTimeField(blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    due_date_of_remittance = models.DateTimeField(blank=True, null=True)
    actual_date_of_remittance = models.DateTimeField(blank=True, null=True)
    invoice_date = models.DateTimeField(blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_reference_no = models.CharField(max_length=255, blank=True, null=True)
    transaction_mode = models.CharField(max_length=255, blank=True, null=True)
    cod_amount = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courier_cod_remittance_log'


class CourierPreferences(models.Model):
    seller_id = models.IntegerField()
    payment_mode = models.CharField(max_length=100, blank=True, null=True)
    order_amount = models.CharField(max_length=100, blank=True, null=True)
    pickup_pincode = models.CharField(max_length=100, blank=True, null=True)
    delivery_pincode = models.CharField(max_length=100, blank=True, null=True)
    zone = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_sku = models.CharField(max_length=100, blank=True, null=True)
    conditional_attribute = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courier_preferences'


class Coverage(models.Model):
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coverage'


class CronJobs(models.Model):
    job_name = models.CharField(unique=True, max_length=255)
    cron_url = models.TextField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    last_status = models.CharField(max_length=25, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cron_jobs'


class CronLogs(models.Model):
    cron_name = models.CharField(max_length=255)
    status = models.CharField(max_length=25, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    success = models.TextField(blank=True, null=True)
    errors = models.TextField(blank=True, null=True)
    row_inserted = models.IntegerField(blank=True, null=True)
    row_updated = models.IntegerField(blank=True, null=True)
    row_deleted = models.IntegerField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cron_logs'


class CustomerChannels(models.Model):
    seller_id = models.IntegerField()
    channel_name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100)
    store_url = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_channels'


class DelhiveryAwbNumbers(models.Model):
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    used = models.CharField(max_length=1, blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    seller_type = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delhivery_awb_numbers'


class Dimensions(models.Model):
    weight = models.IntegerField()
    length = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dimensions'


class DownloadOrderReport(models.Model):
    report_name = models.CharField(max_length=100, blank=True, null=True)
    report_download_url = models.TextField(blank=True, null=True)
    payload = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'download_order_report'


class DownloadReport(models.Model):
    seller_id = models.IntegerField()
    report_name = models.CharField(max_length=255)
    report_type = models.CharField(max_length=255, blank=True, null=True)
    report_status = models.CharField(max_length=255)
    report_download_url = models.TextField(blank=True, null=True)
    extra_urls = models.TextField(blank=True, null=True)
    payload = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    bucket_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'download_report'


class DtdcAwbNumbers(models.Model):
    awb_number = models.CharField(max_length=20)
    used = models.CharField(max_length=1)
    used_time = models.DateTimeField(blank=True, null=True)
    used_by = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    seller_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dtdc_awb_numbers'


class DtdcPushDataLog(models.Model):
    awb = models.CharField(max_length=20, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    inserted = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dtdc_push_data_log'


class EarlyCod(models.Model):
    title = models.TextField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    number_of_days = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'early_cod'


class EcomExpressAwbs(models.Model):
    courier_partner = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    awb_number = models.CharField(max_length=30)
    used = models.CharField(max_length=1)
    used_by = models.IntegerField()
    used_time = models.DateTimeField(blank=True, null=True)
    generated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecom_express_awbs'


class EkartAwbNumbers(models.Model):
    number = models.CharField(max_length=10)
    used = models.CharField(max_length=1)
    awb_number = models.CharField(max_length=20, blank=True, null=True)
    courier_partner = models.CharField(max_length=255, blank=True, null=True)
    generated_id = models.IntegerField(blank=True, null=True)
    generated = models.DateTimeField(blank=True, null=True)
    assigned = models.CharField(max_length=255, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    used_by = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ekart_awb_numbers'


class EmployeeWorkLogs(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    operation = models.CharField(max_length=6, blank=True, null=True)
    inserted = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employee_work_logs'


class Employees(models.Model):
    seller_id = models.IntegerField()
    code = models.CharField(max_length=30, blank=True, null=True)
    employee_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    permissions = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Features(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'features'


class FileUploadJob(models.Model):
    job_name = models.CharField(max_length=255)
    total_records = models.IntegerField(blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    failed = models.IntegerField(blank=True, null=True)
    already_uploaded = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_upload_job'


class FileUploadJobLog(models.Model):
    job_id = models.IntegerField()
    awb_number = models.CharField(max_length=255)
    weight = models.CharField(max_length=255, blank=True, null=True)
    length = models.CharField(max_length=255, blank=True, null=True)
    breadth = models.CharField(max_length=255, blank=True, null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    cod_transactions_id = models.CharField(max_length=255, blank=True, null=True)
    crf_id = models.CharField(max_length=255, blank=True, null=True)
    cod_amount = models.CharField(max_length=255, blank=True, null=True)
    remittance_amount = models.CharField(max_length=255, blank=True, null=True)
    utr_number = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_upload_job_log'


class GatiAwbs(models.Model):
    courier_partner = models.CharField(max_length=50)
    awb_number = models.CharField(max_length=30)
    used = models.CharField(max_length=1)
    used_by = models.IntegerField(blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    assigned = models.CharField(max_length=1, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    generated_id = models.IntegerField(blank=True, null=True)
    generated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gati_awbs'


class GatiPackageNumbers(models.Model):
    courier_partner = models.CharField(max_length=50)
    package_number = models.CharField(max_length=30)
    used = models.CharField(max_length=1)
    used_by = models.IntegerField(blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    assigned = models.CharField(max_length=1, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    generated_id = models.IntegerField(blank=True, null=True)
    generated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gati_package_numbers'


class GeneratedAwb(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    no_of_awb = models.IntegerField(blank=True, null=True)
    partner_id = models.CharField(max_length=100, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generated_awb'


class InternationalOrders(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    invoice_number = models.CharField(max_length=40, blank=True, null=True)
    iec_code = models.CharField(max_length=50, blank=True, null=True)
    ad_code = models.CharField(max_length=50, blank=True, null=True)
    ioss = models.CharField(max_length=50, blank=True, null=True)
    eori = models.CharField(max_length=50, blank=True, null=True)
    hsn = models.CharField(max_length=50, blank=True, null=True)
    hts = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'international_orders'


class IntransitOrdersList(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    from_status = models.CharField(max_length=30, blank=True, null=True)
    to_status = models.CharField(max_length=30, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intransit_orders_list'


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


class JobBatches(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    total_jobs = models.IntegerField()
    pending_jobs = models.IntegerField()
    failed_jobs = models.IntegerField()
    failed_job_ids = models.TextField()
    options = models.TextField(blank=True, null=True)
    cancelled_at = models.IntegerField(blank=True, null=True)
    created_at = models.IntegerField()
    finished_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_batches'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class KycInformation(models.Model):
    seller_id = models.IntegerField()
    document_upload = models.TextField(blank=True, null=True)
    company_type = models.CharField(max_length=100, blank=True, null=True)
    document_type = models.CharField(max_length=100, blank=True, null=True)
    document_id = models.CharField(max_length=100, blank=True, null=True)
    document_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kyc_information'


class LabelCustomizations(models.Model):
    seller_id = models.IntegerField()
    header_visibility = models.CharField(max_length=1, blank=True, null=True)
    shipping_address_visibility = models.CharField(max_length=1, blank=True, null=True)
    billing_address_visibility = models.CharField(max_length=1, blank=True, null=True)
    header_logo_visibility = models.CharField(max_length=1, blank=True, null=True)
    shipment_detail_visibility = models.CharField(max_length=1, blank=True, null=True)
    awb_barcode_visibility = models.CharField(max_length=1, blank=True, null=True)
    order_detail_visibility = models.CharField(max_length=1, blank=True, null=True)
    order_barcode_visibility = models.CharField(max_length=1, blank=True, null=True)
    product_detail_visibility = models.CharField(max_length=1, blank=True, null=True)
    invoice_value_visibility = models.CharField(max_length=1, blank=True, null=True)
    gift_visibility = models.CharField(max_length=1, blank=True, null=True)
    footer_visibility = models.CharField(max_length=1, blank=True, null=True)
    display_full_product_name = models.CharField(max_length=1, blank=True, null=True)
    disclaimer_text = models.CharField(max_length=1, blank=True, null=True)
    other_charges = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label_customizations'


class LogisticPartners(models.Model):
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'logistic_partners'


class Manifest(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    courier = models.CharField(max_length=50, blank=True, null=True)
    number_of_order = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    warehouse_name = models.TextField(blank=True, null=True)
    warehouse_address = models.TextField(blank=True, null=True)
    warehouse_contact = models.CharField(max_length=15, blank=True, null=True)
    warehouse_gst_no = models.CharField(max_length=20, blank=True, null=True)
    p_ref_no = models.CharField(max_length=30, blank=True, null=True)
    created = models.DateField(blank=True, null=True)
    created_time = models.TimeField(blank=True, null=True)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'manifest'


class ManifestOrder(models.Model):
    manifest_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manifest_order'


class ManifestOrderDeleted(models.Model):
    manifest_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manifest_order_deleted'


class MarutiAwbs(models.Model):
    courier_partner = models.CharField(max_length=50)
    awb_number = models.CharField(max_length=30)
    used = models.CharField(max_length=1)
    used_by = models.IntegerField(blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    assigned = models.CharField(max_length=1, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    generated_id = models.IntegerField(blank=True, null=True)
    generated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maruti_awbs'


class MarutiAwbsEcom(models.Model):
    courier_partner = models.CharField(max_length=50)
    awb_number = models.CharField(max_length=30)
    used = models.CharField(max_length=1)
    used_by = models.IntegerField(blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    assigned = models.CharField(max_length=1, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    generated_id = models.IntegerField(blank=True, null=True)
    generated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maruti_awbs_ecom'


class Master(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100, blank=True, null=True)
    link = models.TextField()
    icon = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1)
    inserted_by = models.IntegerField(blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class MovinAwbNumbers(models.Model):
    awb_number = models.CharField(unique=True, max_length=50, blank=True, null=True)
    used = models.CharField(max_length=1, blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    mode = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'movin_awb_numbers'


class MpsAwbNumber(models.Model):
    order_id = models.IntegerField()
    awb_number = models.CharField(max_length=250)
    inserted = models.DateTimeField(blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    awb_barcode = models.TextField(blank=True, null=True)
    gati_ou_code = models.CharField(max_length=255, blank=True, null=True)
    gati_package_no = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mps_awb_number'


class MyOmsOrderProducts(models.Model):
    order_id = models.IntegerField()
    product_sku = models.TextField(blank=True, null=True)
    product_name = models.TextField()
    product_unitprice = models.CharField(max_length=10, blank=True, null=True)
    product_qty = models.CharField(max_length=10, blank=True, null=True)
    total_amount = models.CharField(max_length=10, blank=True, null=True)
    item_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'my_oms_order_products'


class MyOmsOrders(models.Model):
    order_number = models.CharField(max_length=30, blank=True, null=True)
    customer_order_number = models.CharField(max_length=30)
    seller_id = models.IntegerField(blank=True, null=True)
    warehouse_id = models.IntegerField(blank=True, null=True)
    order_type = models.CharField(max_length=50, blank=True, null=True)
    o_type = models.CharField(max_length=10, blank=True, null=True)
    b_customer_name = models.TextField(blank=True, null=True)
    b_customer_email = models.TextField(blank=True, null=True)
    b_address_line1 = models.TextField(blank=True, null=True)
    b_address_line2 = models.TextField(blank=True, null=True)
    b_country = models.CharField(max_length=40, blank=True, null=True)
    b_state = models.CharField(max_length=40, blank=True, null=True)
    b_city = models.CharField(max_length=40, blank=True, null=True)
    b_pincode = models.CharField(max_length=10, blank=True, null=True)
    b_contact = models.CharField(max_length=15, blank=True, null=True)
    b_contact_code = models.CharField(max_length=5, blank=True, null=True)
    p_warehouse_name = models.TextField(blank=True, null=True)
    p_customer_name = models.TextField(blank=True, null=True)
    p_address_line1 = models.TextField(blank=True, null=True)
    p_address_line2 = models.TextField(blank=True, null=True)
    p_country = models.CharField(max_length=50, blank=True, null=True)
    p_state = models.CharField(max_length=50, blank=True, null=True)
    p_city = models.CharField(max_length=50, blank=True, null=True)
    p_pincode = models.CharField(max_length=10, blank=True, null=True)
    p_contact = models.CharField(max_length=15, blank=True, null=True)
    p_contact_code = models.CharField(max_length=5, blank=True, null=True)
    s_customer_name = models.TextField(blank=True, null=True)
    s_address_line1 = models.TextField(blank=True, null=True)
    s_address_line2 = models.TextField(blank=True, null=True)
    s_country = models.CharField(max_length=50, blank=True, null=True)
    s_state = models.CharField(max_length=50, blank=True, null=True)
    s_city = models.CharField(max_length=50, blank=True, null=True)
    s_pincode = models.CharField(max_length=10, blank=True, null=True)
    s_contact = models.CharField(max_length=15, blank=True, null=True)
    s_contact_code = models.CharField(max_length=5, blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)
    length = models.CharField(max_length=20, blank=True, null=True)
    breadth = models.CharField(max_length=20, blank=True, null=True)
    height = models.CharField(max_length=20, blank=True, null=True)
    vol_weight = models.FloatField()
    invoice_amount = models.CharField(max_length=10, blank=True, null=True)
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    awb_assigned_date = models.DateTimeField(blank=True, null=True)
    awb_barcode = models.TextField(blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    product_sku = models.TextField(blank=True, null=True)
    pickup_address = models.TextField(blank=True, null=True)
    delivery_address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50)
    orderno_barcode = models.TextField(blank=True, null=True)
    reseller_name = models.CharField(max_length=50, blank=True, null=True)
    suggested_awb = models.CharField(max_length=100, blank=True, null=True)
    product_qty = models.IntegerField()
    shipment_type = models.CharField(max_length=10, blank=True, null=True)
    number_of_packets = models.IntegerField(blank=True, null=True)
    is_master = models.CharField(max_length=10, blank=True, null=True)
    parent_id = models.PositiveBigIntegerField(blank=True, null=True)
    master_id = models.TextField(blank=True, null=True)
    route_code = models.CharField(max_length=100, blank=True, null=True)
    ewaybill_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_oms_orders'


class NdrAttemps(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    raised_date = models.TextField(blank=True, null=True)
    raised_time = models.TimeField(blank=True, null=True)
    action_by = models.CharField(max_length=50, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    action_date = models.TextField(blank=True, null=True)
    action_status = models.CharField(max_length=50, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    u_address_line1 = models.TextField(blank=True, null=True)
    u_address_line2 = models.TextField(blank=True, null=True)
    updated_mobile = models.CharField(max_length=15, blank=True, null=True)
    ndr_data_type = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ndr_attemps'


class Newsletter(models.Model):
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter'


class Notifications(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    type = models.CharField(max_length=255)
    notifiable_type = models.CharField(max_length=255)
    notifiable_id = models.PositiveBigIntegerField()
    data = models.TextField()
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class Oms(models.Model):
    seller_id = models.IntegerField()
    oms_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    store_url = models.TextField(blank=True, null=True)
    easyship_bearer_token = models.TextField(blank=True, null=True)
    easyecom_api_token = models.TextField(blank=True, null=True)
    clickpost_username = models.TextField(blank=True, null=True)
    clickpost_key = models.TextField(blank=True, null=True)
    vineretail_api_owner = models.TextField(blank=True, null=True)
    vineretail_api_key = models.TextField(blank=True, null=True)
    auto_fulfill = models.CharField(max_length=1, blank=True, null=True)
    auto_cancel = models.CharField(max_length=1, blank=True, null=True)
    auto_cod_paid = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField()
    inserted_by = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    easycom_username = models.CharField(max_length=100, blank=True, null=True)
    easycom_password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms'


class OndcOrderPartner(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    courier_partner = models.CharField(max_length=200, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ondc_order_partner'


class OndcSeller(models.Model):
    domain = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    bap_id = models.CharField(max_length=100, blank=True, null=True)
    bap_uri = models.CharField(max_length=300, blank=True, null=True)
    bpp_id = models.CharField(max_length=100, blank=True, null=True)
    bpp_uri = models.CharField(max_length=300, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, blank=True, null=True)
    message_id = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    ttl = models.TextField(blank=True, null=True)
    balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=1)
    created = models.DateTimeField(blank=True, null=True)
    last_active = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ondc_seller'


class OrderSmsLogs(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    awb_number = models.CharField(max_length=30, blank=True, null=True)
    order_status = models.CharField(max_length=20, blank=True, null=True)
    sent = models.CharField(max_length=1, blank=True, null=True)
    sent_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_sms_logs'


class OrderTracking(models.Model):
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    status_code = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    status_description = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    updated_date = models.TextField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_tracking'


class Orders(models.Model):
    order_number = models.CharField(max_length=30, blank=True, null=True)
    customer_order_number = models.CharField(max_length=30)
    seller_id = models.IntegerField(blank=True, null=True)
    warehouse_id = models.IntegerField(blank=True, null=True)
    order_type = models.CharField(max_length=50, blank=True, null=True)
    o_type = models.CharField(max_length=10, blank=True, null=True)
    b_customer_name = models.TextField(blank=True, null=True)
    b_customer_email = models.TextField(blank=True, null=True)
    b_address_line1 = models.TextField(blank=True, null=True)
    b_address_line2 = models.TextField(blank=True, null=True)
    b_country = models.CharField(max_length=40, blank=True, null=True)
    b_state = models.CharField(max_length=40, blank=True, null=True)
    b_city = models.CharField(max_length=40, blank=True, null=True)
    b_pincode = models.CharField(max_length=10, blank=True, null=True)
    b_contact = models.CharField(max_length=15, blank=True, null=True)
    b_contact_code = models.CharField(max_length=5, blank=True, null=True)
    p_warehouse_name = models.TextField(blank=True, null=True)
    p_customer_name = models.TextField(blank=True, null=True)
    p_address_line1 = models.TextField(blank=True, null=True)
    p_address_line2 = models.TextField(blank=True, null=True)
    p_country = models.CharField(max_length=50, blank=True, null=True)
    p_state = models.CharField(max_length=50, blank=True, null=True)
    p_city = models.CharField(max_length=50, blank=True, null=True)
    p_pincode = models.CharField(max_length=10, blank=True, null=True)
    p_contact = models.CharField(max_length=15, blank=True, null=True)
    p_contact_code = models.CharField(max_length=5, blank=True, null=True)
    s_customer_name = models.TextField(blank=True, null=True)
    s_address_line1 = models.TextField(blank=True, null=True)
    s_address_line2 = models.TextField(blank=True, null=True)
    s_country = models.CharField(max_length=50, blank=True, null=True)
    s_state = models.CharField(max_length=50, blank=True, null=True)
    s_city = models.CharField(max_length=50, blank=True, null=True)
    s_pincode = models.CharField(max_length=10, blank=True, null=True)
    s_contact = models.CharField(max_length=15, blank=True, null=True)
    s_contact_code = models.CharField(max_length=5, blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)
    length = models.CharField(max_length=20, blank=True, null=True)
    breadth = models.CharField(max_length=20, blank=True, null=True)
    height = models.CharField(max_length=20, blank=True, null=True)
    vol_weight = models.FloatField()
    c_weight = models.IntegerField(blank=True, null=True)
    c_length = models.IntegerField(blank=True, null=True)
    c_breadth = models.IntegerField(blank=True, null=True)
    c_height = models.IntegerField(blank=True, null=True)
    s_charge = models.CharField(max_length=10, blank=True, null=True)
    c_charge = models.CharField(max_length=10, blank=True, null=True)
    shipping_charges = models.FloatField(blank=True, null=True)
    cod_charges = models.FloatField(blank=True, null=True)
    cod_maintenence = models.FloatField(blank=True, null=True)
    rto_charges = models.CharField(max_length=10, blank=True, null=True)
    total_charges = models.CharField(max_length=10, blank=True, null=True)
    early_cod_charges = models.FloatField(blank=True, null=True)
    gst_charges = models.FloatField(blank=True, null=True)
    excess_weight_charges = models.CharField(max_length=10, blank=True, null=True)
    discount = models.CharField(max_length=10, blank=True, null=True)
    invoice_amount = models.CharField(max_length=10, blank=True, null=True)
    cgst = models.FloatField(blank=True, null=True)
    sgst = models.FloatField(blank=True, null=True)
    igst = models.FloatField(blank=True, null=True)
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    alternate_awb_number = models.CharField(max_length=30, blank=True, null=True)
    xb_token_number = models.CharField(max_length=50, blank=True, null=True)
    awb_assigned_date = models.DateTimeField(blank=True, null=True)
    awb_barcode = models.TextField(blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    product_sku = models.TextField(blank=True, null=True)
    pickup_address = models.TextField(blank=True, null=True)
    delivery_address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50)
    delivery_stutus = models.CharField(max_length=50, blank=True, null=True)
    escalation_status = models.CharField(max_length=50, blank=True, null=True)
    ndr_action = models.CharField(max_length=50, blank=True, null=True)
    ndr_status = models.CharField(max_length=50, blank=True, null=True)
    rto_status = models.CharField(max_length=20, blank=True, null=True)
    pickup_time = models.CharField(max_length=50, blank=True, null=True)
    pickup_done = models.CharField(max_length=10, blank=True, null=True)
    pickup_schedule = models.CharField(max_length=1, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    manifest_status = models.CharField(max_length=1, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    reason_for_cancel = models.TextField(blank=True, null=True)
    reason_for_ndr = models.TextField(blank=True, null=True)
    reason_for_delay = models.TextField(blank=True, null=True)
    orderno_barcode = models.TextField(blank=True, null=True)
    zone = models.CharField(max_length=5, blank=True, null=True)
    invoice_status = models.CharField(max_length=1)
    delivered_date = models.DateTimeField(blank=True, null=True)
    expected_delivery_date = models.DateField(blank=True, null=True)
    last_sync = models.DateTimeField()
    ndr_status_date = models.CharField(max_length=50, blank=True, null=True)
    cod_remmited = models.CharField(max_length=1)
    reseller_name = models.CharField(max_length=50, blank=True, null=True)
    weight_disputed = models.CharField(max_length=1)
    settled_weight_disputed = models.CharField(max_length=1, blank=True, null=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    last_verified = models.DateTimeField(blank=True, null=True)
    fulfillment_id = models.CharField(max_length=50, blank=True, null=True)
    location_id = models.CharField(max_length=50, blank=True, null=True)
    seller_channel_id = models.IntegerField(blank=True, null=True)
    seller_channel_name = models.CharField(max_length=255, blank=True, null=True)
    suggested_awb = models.CharField(max_length=100, blank=True, null=True)
    reference_code = models.TextField(blank=True, null=True)
    marketplace = models.TextField(blank=True, null=True)
    marketplace_id = models.TextField(blank=True, null=True)
    amazon_order_id = models.IntegerField(blank=True, null=True)
    manifest_sent = models.CharField(max_length=1, blank=True, null=True)
    product_qty = models.IntegerField()
    fulfillment_sent = models.CharField(max_length=1)
    imported = models.DateTimeField(blank=True, null=True)
    weight_updated = models.CharField(max_length=1, blank=True, null=True)
    amazon_shipment_id = models.CharField(max_length=200, blank=True, null=True)
    amazon_label = models.TextField(blank=True, null=True)
    shipment_type = models.CharField(max_length=10, blank=True, null=True)
    number_of_packets = models.IntegerField(blank=True, null=True)
    is_master = models.CharField(max_length=10, blank=True, null=True)
    parent_id = models.PositiveBigIntegerField(blank=True, null=True)
    master_id = models.TextField(blank=True, null=True)
    bluedart_label = models.TextField(blank=True, null=True)
    route_code = models.CharField(max_length=100, blank=True, null=True)
    ewaybill_number = models.CharField(max_length=50, blank=True, null=True)
    shipping_partner = models.CharField(max_length=25, blank=True, null=True)
    ndr_raised_time = models.DateTimeField(blank=True, null=True)
    seller_order_type = models.CharField(max_length=3)
    last_executed = models.DateTimeField(blank=True, null=True)
    gati_ou_code = models.CharField(max_length=255, blank=True, null=True)
    gati_package_no = models.CharField(max_length=255, blank=True, null=True)
    is_tagged = models.CharField(max_length=1, blank=True, null=True)
    global_type = models.CharField(max_length=30)
    same_as_rto = models.CharField(max_length=1, blank=True, null=True)
    rto_warehouse_id = models.IntegerField(blank=True, null=True)
    ondc_seller_id = models.IntegerField(blank=True, null=True)
    channel_name = models.CharField(max_length=100, blank=True, null=True)
    is_qc = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'orders'
        unique_together = (('channel_id', 'channel', 'seller_id'),)


class OrdersDeleted(models.Model):
    id = models.IntegerField()
    order_number = models.CharField(max_length=30, blank=True, null=True)
    customer_order_number = models.CharField(max_length=30)
    seller_id = models.IntegerField(blank=True, null=True)
    warehouse_id = models.IntegerField(blank=True, null=True)
    order_type = models.CharField(max_length=50, blank=True, null=True)
    o_type = models.CharField(max_length=10, blank=True, null=True)
    b_customer_name = models.TextField(blank=True, null=True)
    b_customer_email = models.TextField(blank=True, null=True)
    b_address_line1 = models.TextField(blank=True, null=True)
    b_address_line2 = models.TextField(blank=True, null=True)
    b_country = models.CharField(max_length=40, blank=True, null=True)
    b_state = models.CharField(max_length=40, blank=True, null=True)
    b_city = models.CharField(max_length=40, blank=True, null=True)
    b_pincode = models.CharField(max_length=10, blank=True, null=True)
    b_contact = models.CharField(max_length=15, blank=True, null=True)
    b_contact_code = models.CharField(max_length=5, blank=True, null=True)
    p_warehouse_name = models.TextField(blank=True, null=True)
    p_customer_name = models.TextField(blank=True, null=True)
    p_address_line1 = models.TextField(blank=True, null=True)
    p_address_line2 = models.TextField(blank=True, null=True)
    p_country = models.CharField(max_length=50, blank=True, null=True)
    p_state = models.CharField(max_length=50, blank=True, null=True)
    p_city = models.CharField(max_length=50, blank=True, null=True)
    p_pincode = models.CharField(max_length=10, blank=True, null=True)
    p_contact = models.CharField(max_length=15, blank=True, null=True)
    p_contact_code = models.CharField(max_length=5, blank=True, null=True)
    s_customer_name = models.TextField(blank=True, null=True)
    s_address_line1 = models.TextField(blank=True, null=True)
    s_address_line2 = models.TextField(blank=True, null=True)
    s_country = models.CharField(max_length=50, blank=True, null=True)
    s_state = models.CharField(max_length=50, blank=True, null=True)
    s_city = models.CharField(max_length=50, blank=True, null=True)
    s_pincode = models.CharField(max_length=10, blank=True, null=True)
    s_contact = models.CharField(max_length=15, blank=True, null=True)
    s_contact_code = models.CharField(max_length=5, blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)
    length = models.CharField(max_length=20, blank=True, null=True)
    breadth = models.CharField(max_length=20, blank=True, null=True)
    height = models.CharField(max_length=20, blank=True, null=True)
    vol_weight = models.FloatField(blank=True, null=True)
    c_weight = models.IntegerField(blank=True, null=True)
    c_length = models.IntegerField(blank=True, null=True)
    c_breadth = models.IntegerField(blank=True, null=True)
    c_height = models.IntegerField(blank=True, null=True)
    s_charge = models.CharField(max_length=10, blank=True, null=True)
    c_charge = models.CharField(max_length=10, blank=True, null=True)
    shipping_charges = models.FloatField(blank=True, null=True)
    cod_charges = models.FloatField(blank=True, null=True)
    cod_maintenence = models.FloatField(blank=True, null=True)
    rto_charges = models.CharField(max_length=10, blank=True, null=True)
    total_charges = models.CharField(max_length=10, blank=True, null=True)
    early_cod_charges = models.FloatField(blank=True, null=True)
    gst_charges = models.FloatField(blank=True, null=True)
    excess_weight_charges = models.CharField(max_length=10, blank=True, null=True)
    discount = models.CharField(max_length=10, blank=True, null=True)
    invoice_amount = models.CharField(max_length=10, blank=True, null=True)
    cgst = models.IntegerField(blank=True, null=True)
    sgst = models.IntegerField(blank=True, null=True)
    igst = models.IntegerField(blank=True, null=True)
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    xb_token_number = models.CharField(max_length=50, blank=True, null=True)
    awb_assigned_date = models.DateTimeField(blank=True, null=True)
    awb_barcode = models.TextField(blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    product_sku = models.TextField(blank=True, null=True)
    pickup_address = models.TextField(blank=True, null=True)
    delivery_address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    delivery_stutus = models.CharField(max_length=50, blank=True, null=True)
    escalation_status = models.CharField(max_length=50, blank=True, null=True)
    ndr_action = models.CharField(max_length=50, blank=True, null=True)
    ndr_status = models.CharField(max_length=50, blank=True, null=True)
    rto_status = models.CharField(max_length=20, blank=True, null=True)
    pickup_time = models.CharField(max_length=50, blank=True, null=True)
    pickup_done = models.CharField(max_length=10, blank=True, null=True)
    pickup_schedule = models.CharField(max_length=1, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    manifest_status = models.CharField(max_length=1, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    reason_for_cancel = models.TextField(blank=True, null=True)
    reason_for_ndr = models.TextField(blank=True, null=True)
    reason_for_delay = models.TextField(blank=True, null=True)
    orderno_barcode = models.TextField(blank=True, null=True)
    zone = models.CharField(max_length=5, blank=True, null=True)
    invoice_status = models.CharField(max_length=1)
    delivered_date = models.DateTimeField(blank=True, null=True)
    expected_delivery_date = models.DateField(blank=True, null=True)
    last_sync = models.DateTimeField()
    ndr_status_date = models.CharField(max_length=20, blank=True, null=True)
    cod_remmited = models.CharField(max_length=1, blank=True, null=True)
    reseller_name = models.CharField(max_length=50, blank=True, null=True)
    weight_disputed = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders_deleted'


class Partners(models.Model):
    parent_id = models.IntegerField()
    title = models.CharField(max_length=60)
    keyword = models.CharField(max_length=100, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    api_key = models.TextField(blank=True, null=True)
    other_key = models.TextField(blank=True, null=True)
    ship_url = models.TextField(blank=True, null=True)
    track_url = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    weight_initial = models.IntegerField()
    extra_limit = models.IntegerField()
    serviceability_check = models.CharField(max_length=50, blank=True, null=True)
    zone_a = models.IntegerField()
    zone_b = models.IntegerField()
    zone_c = models.IntegerField()
    zone_d = models.IntegerField()
    zone_e = models.IntegerField()
    mps_enabled = models.CharField(max_length=10, blank=True, null=True)
    reverse_enabled = models.CharField(max_length=25, blank=True, null=True)
    liability_amount = models.FloatField(blank=True, null=True)
    weight_category = models.CharField(max_length=20, blank=True, null=True)
    international_enabled = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partners'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PendingShipments(models.Model):
    seller_id = models.IntegerField()
    order_id = models.IntegerField()
    status = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    last_tried = models.DateTimeField(blank=True, null=True)
    notified = models.CharField(max_length=1, blank=True, null=True)
    shipped = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pending_shipments'


class PickedOrdersList(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    from_status = models.CharField(max_length=30, blank=True, null=True)
    to_status = models.CharField(max_length=30, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picked_orders_list'


class PincodeDistance(models.Model):
    pincode1 = models.CharField(max_length=6, blank=True, null=True)
    pincode2 = models.CharField(max_length=6, blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    payload = models.TextField(blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pincode_distance'


class PlanFeatures(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan_features'


class Plans(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plans'


class Preferences(models.Model):
    seller_id = models.IntegerField()
    rule_name = models.CharField(max_length=50)
    priority = models.IntegerField()
    match_type = models.CharField(max_length=10)
    priority1 = models.CharField(max_length=50)
    priority2 = models.CharField(max_length=50)
    priority3 = models.CharField(max_length=50)
    priority4 = models.CharField(max_length=50)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preferences'


class Products(models.Model):
    order_id = models.IntegerField()
    product_sku = models.TextField(blank=True, null=True)
    product_name = models.TextField()
    product_unitprice = models.CharField(max_length=10, blank=True, null=True)
    product_qty = models.CharField(max_length=10, blank=True, null=True)
    total_amount = models.CharField(max_length=10, blank=True, null=True)
    item_id = models.CharField(max_length=50)
    invoice_reference_number = models.CharField(max_length=60, blank=True, null=True)
    export_reference_number = models.CharField(max_length=60, blank=True, null=True)
    hsn_number = models.CharField(max_length=50, blank=True, null=True)
    hts_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Rates(models.Model):
    plan_id = models.IntegerField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    partner_id = models.IntegerField(blank=True, null=True)
    within_city = models.FloatField(blank=True, null=True)
    within_state = models.FloatField(blank=True, null=True)
    metro_to_metro = models.FloatField(blank=True, null=True)
    rest_india = models.FloatField(blank=True, null=True)
    north_j_k = models.FloatField(blank=True, null=True)
    cod_charge = models.FloatField(blank=True, null=True)
    cod_maintenance = models.FloatField(blank=True, null=True)
    extra_charge_a = models.FloatField(blank=True, null=True)
    extra_charge_b = models.FloatField(blank=True, null=True)
    extra_charge_c = models.FloatField(blank=True, null=True)
    extra_charge_d = models.FloatField(blank=True, null=True)
    extra_charge_e = models.FloatField(blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rates'


class ReceiptDetails(models.Model):
    receipt_id = models.IntegerField(blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receipt_details'


class RechargeRequest(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    utr_number = models.CharField(max_length=30, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    created = models.DateTimeField(blank=True, null=True)
    approved = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recharge_request'


class RecommendationEngine(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recommendation_engine'


class RedeemCodes(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redeem_codes'


class Redeems(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    code_id = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    redeemed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redeems'


class RemittanceDetails(models.Model):
    cod_transactions_id = models.IntegerField(blank=True, null=True)
    crf_id = models.IntegerField(blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    order_number = models.CharField(max_length=50, blank=True, null=True)
    cod_amount = models.IntegerField(blank=True, null=True)
    remittance_amount = models.IntegerField(blank=True, null=True)
    utr_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remittance_details'


class Rules(models.Model):
    preferences_id = models.IntegerField()
    criteria = models.CharField(max_length=100)
    match_type = models.CharField(max_length=100)
    match_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'rules'


class SellerOtp(models.Model):
    mobile = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seller_otp'


class SellerPartners(models.Model):
    seller_id = models.IntegerField()
    partner_id = models.IntegerField()
    partner_keyword = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    api_key = models.CharField(max_length=255, blank=True, null=True)
    client_id = models.CharField(max_length=255, blank=True, null=True)
    client_key = models.CharField(max_length=255, blank=True, null=True)
    client_secret = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    app_id = models.CharField(max_length=255, blank=True, null=True)
    login_id = models.CharField(max_length=255, blank=True, null=True)
    login_name = models.CharField(max_length=255, blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    licence_key = models.CharField(max_length=255, blank=True, null=True)
    customer_code = models.CharField(max_length=255, blank=True, null=True)
    shipping_agent_code = models.CharField(max_length=255, blank=True, null=True)
    session_id = models.CharField(max_length=255, blank=True, null=True)
    awb_prefix = models.CharField(max_length=255, blank=True, null=True)
    grant_type = models.CharField(max_length=255, blank=True, null=True)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    access_key = models.CharField(max_length=255, blank=True, null=True)
    secret_key = models.CharField(max_length=255, blank=True, null=True)
    aws_region = models.CharField(max_length=255, blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    service_type = models.CharField(max_length=255, blank=True, null=True)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    xb_key = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    api_type = models.CharField(max_length=255, blank=True, null=True)
    api_version = models.CharField(max_length=255, blank=True, null=True)
    weight_initial = models.FloatField(blank=True, null=True)
    extra_limit = models.FloatField(blank=True, null=True)
    within_city = models.FloatField(blank=True, null=True)
    within_state = models.FloatField(blank=True, null=True)
    metro_to_metro = models.FloatField(blank=True, null=True)
    rest_india = models.FloatField(blank=True, null=True)
    north_j_k = models.FloatField(blank=True, null=True)
    cod_charge = models.FloatField(blank=True, null=True)
    cod_maintenance = models.FloatField(blank=True, null=True)
    extra_charge_a = models.FloatField(blank=True, null=True)
    extra_charge_b = models.FloatField(blank=True, null=True)
    extra_charge_c = models.FloatField(blank=True, null=True)
    extra_charge_d = models.FloatField(blank=True, null=True)
    extra_charge_e = models.FloatField(blank=True, null=True)
    mps_enabled = models.CharField(max_length=1)
    reverse_enabled = models.CharField(max_length=1)
    liability_amount = models.FloatField()
    status = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seller_partners'


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
    remmitnace_frequency = models.IntegerField(blank=True, null=True)
    brand_tracking_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sellers'


class ServiceablePincode(models.Model):
    partner_id = models.IntegerField(blank=True, null=True)
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.BigIntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    branch_code = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    active = models.CharField(max_length=1)
    modified = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serviceable_pincode'


class ServiceablePincodeFm(models.Model):
    partner_id = models.IntegerField(blank=True, null=True)
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.BigIntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    branch_code = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serviceable_pincode_fm'


class ShadowfaxAwbNumbers(models.Model):
    awb_number = models.CharField(unique=True, max_length=30, blank=True, null=True)
    flow = models.CharField(max_length=7, blank=True, null=True)
    used = models.CharField(max_length=1)
    seller_id = models.IntegerField(blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    used_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadowfax_awb_numbers'


class ShopifyAbandonSmsLog(models.Model):
    channel_id = models.IntegerField(blank=True, null=True)
    abandon_id = models.CharField(max_length=255, blank=True, null=True)
    abandoned_checkout_url = models.TextField(blank=True, null=True)
    sub_total_amount = models.IntegerField(blank=True, null=True)
    presentment_currency = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    sms_status = models.CharField(max_length=255, blank=True, null=True)
    sms_charge = models.IntegerField(blank=True, null=True)
    sms_sent_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopify_abandon_sms_log'


class Sku(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    sku = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    brand_name = models.CharField(max_length=100, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sku'
        unique_together = (('seller_id', 'sku', 'product_name'),)


class SkuMapping(models.Model):
    seller_id = models.IntegerField()
    parent_sku = models.CharField(max_length=255, blank=True, null=True)
    child_sku = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sku_mapping'


class Slider(models.Model):
    title = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'slider'


class SmartrAwbs(models.Model):
    courier_partner = models.CharField(max_length=50)
    awb_number = models.CharField(max_length=30)
    used = models.CharField(max_length=1)
    used_by = models.IntegerField(blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smartr_awbs'


class SocialLinks(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_links'


class States(models.Model):
    state = models.CharField(max_length=50)
    code = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'states'


class Stats(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats'


class Steps(models.Model):
    image = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'steps'


class SupportSub(models.Model):
    support_id = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'support_sub'


class SupportTicket(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    ticket_no = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    issue = models.TextField(blank=True, null=True)
    awb_number = models.TextField(blank=True, null=True)
    raised = models.DateTimeField(blank=True, null=True)
    last_replied = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    escalate_reason = models.TextField(blank=True, null=True)
    sevierity = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'support_ticket'


class Testimonial(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testimonial'


class TicketAttachment(models.Model):
    ticket_id = models.IntegerField(blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_attachment'


class TicketComments(models.Model):
    ticket_id = models.IntegerField(blank=True, null=True)
    replied_by = models.CharField(max_length=30, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    replied = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_comments'


class Transactions(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField()
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


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class WalletRecharges(models.Model):
    seller_id = models.IntegerField()
    recharge_amount = models.FloatField()
    recharge_mode = models.CharField(max_length=100)
    utr_number = models.CharField(max_length=100)
    datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet_recharges'


class WalletTransactions(models.Model):
    seller_id = models.IntegerField()
    amount = models.FloatField()
    type = models.CharField(max_length=100)
    wallet_balance = models.FloatField()
    datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet_transactions'


class Warehouses(models.Model):
    seller_id = models.IntegerField()
    warehouse_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    address_line1 = models.TextField(blank=True, null=True)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=100, blank=True, null=True)
    gst_number = models.CharField(max_length=100, blank=True, null=True)
    support_email = models.CharField(max_length=200, blank=True, null=True)
    support_phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    default = models.CharField(max_length=1)
    warehouse_code = models.CharField(max_length=100, blank=True, null=True)
    org_unit_id = models.CharField(max_length=50, blank=True, null=True)
    easyecom_warehouse_id = models.CharField(max_length=255, blank=True, null=True)
    pidge_address_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouses'


class WebAboutUs(models.Model):
    image = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    post = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_about_us'


class WebCareer(models.Model):
    image = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_career'


class WebCareerExpect(models.Model):
    image = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=600, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_career_expect'


class WebContactUs(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    company_name = models.CharField(max_length=40, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    monthly_shipment = models.IntegerField()
    city = models.CharField(max_length=30, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    inserted = models.DateTimeField()
    inserted_ip = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_contact_us'


class WebCountryCurrency(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    currency = models.CharField(max_length=200, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_country_currency'


class WebCourier(models.Model):
    image = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_courier'


class WebFaq(models.Model):
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_faq'


class WebFooterConfig(models.Model):
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    mobile1 = models.CharField(max_length=20, blank=True, null=True)
    mobile2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    page = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_footer_config'


class WebFooterSub(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    footer_id = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_footer_sub'


class WebFootercategory(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_footercategory'


class WebGlossary(models.Model):
    title = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    image1 = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    wpr_description = models.TextField(blank=True, null=True)
    lease_description = models.TextField(blank=True, null=True)
    guide_description = models.TextField(blank=True, null=True)
    storage_description = models.TextField(blank=True, null=True)
    termcondiction = models.TextField(blank=True, null=True)
    privacypolicy = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_glossary'


class WebSubscribe(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_subscribe'


class WebSupport(models.Model):
    image = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_support'


class WebSupportChild(models.Model):
    title = models.TextField(blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    support_id = models.CharField(max_length=500, blank=True, null=True)
    supportsub_id = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_support_child'


class WeightReconciliation(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    e_weight = models.FloatField(blank=True, null=True)
    e_length = models.FloatField(blank=True, null=True)
    e_breadth = models.FloatField(blank=True, null=True)
    e_height = models.FloatField(blank=True, null=True)
    applied_amount = models.FloatField(blank=True, null=True)
    c_weight = models.FloatField(blank=True, null=True)
    c_length = models.FloatField(blank=True, null=True)
    c_breadth = models.FloatField(blank=True, null=True)
    c_height = models.FloatField(blank=True, null=True)
    charged_amount = models.FloatField(blank=True, null=True)
    s_weight = models.FloatField(blank=True, null=True)
    s_length = models.FloatField(blank=True, null=True)
    s_breadth = models.FloatField(blank=True, null=True)
    s_height = models.FloatField(blank=True, null=True)
    settled_amount = models.FloatField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    action_taken_by = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    display_status = models.CharField(max_length=1, blank=True, null=True)
    is_error = models.CharField(max_length=25, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weight_reconciliation'


class WeightReconciliationHistory(models.Model):
    weight_reconciliation_id = models.IntegerField(blank=True, null=True)
    action_taken_by = models.CharField(max_length=50, blank=True, null=True)
    history_date = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'weight_reconciliation_history'


class WeightReconciliationImages(models.Model):
    weight_reconciliation_history_id = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weight_reconciliation_images'


class WhyChoose(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'why_choose'


class XbeesAwbNumbers(models.Model):
    order_type = models.CharField(max_length=10, blank=True, null=True)
    batch_number = models.CharField(max_length=20, blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    used = models.CharField(max_length=1, blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    assigned = models.CharField(max_length=1, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    generated_id = models.IntegerField(blank=True, null=True)
    generated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xbees_awb_numbers'


class XbeesAwbNumbersUnique(models.Model):
    order_type = models.CharField(max_length=10, blank=True, null=True)
    batch_number = models.CharField(max_length=20, blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    used = models.CharField(max_length=1, blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    assigned = models.CharField(max_length=1, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    generated_id = models.IntegerField(blank=True, null=True)
    generated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xbees_awb_numbers_unique'


class XindusRates(models.Model):
    weight = models.IntegerField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    is_additional = models.CharField(max_length=1)
    initial_weight = models.IntegerField()
    extra_charge = models.IntegerField(blank=True, null=True)
    extra_limit = models.IntegerField()
    seller_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xindus_rates'


class ZoneMapping(models.Model):
    partner_id = models.IntegerField(blank=True, null=True)
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    has_cod = models.CharField(max_length=10, blank=True, null=True)
    has_dg = models.CharField(max_length=10, blank=True, null=True)
    has_prepaid = models.CharField(max_length=10, blank=True, null=True)
    has_reverse = models.CharField(max_length=10, blank=True, null=True)
    picker_zone = models.CharField(max_length=10, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    routing_code = models.CharField(max_length=10, blank=True, null=True)
    cod_limit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zone_mapping'


class ZzArchiveChannelOrdersLog(models.Model):
    channel = models.CharField(max_length=30, blank=True, null=True)
    channel_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    order_response = models.TextField(blank=True, null=True)
    item_fetched = models.CharField(max_length=1, blank=True, null=True)
    item_response = models.TextField(blank=True, null=True)
    address_fetched = models.CharField(max_length=1, blank=True, null=True)
    address_response = models.TextField(blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_channel_orders_log'


class ZzArchiveCodTransactions(models.Model):
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
        db_table = 'zz_archive_cod_transactions'


class ZzArchiveCronLogs(models.Model):
    cron_name = models.CharField(max_length=255)
    status = models.CharField(max_length=25, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    success = models.TextField(blank=True, null=True)
    errors = models.TextField(blank=True, null=True)
    row_inserted = models.IntegerField(blank=True, null=True)
    row_updated = models.IntegerField(blank=True, null=True)
    row_deleted = models.IntegerField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_cron_logs'


class ZzArchiveDelhiveryAwbNumbers(models.Model):
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    used = models.CharField(max_length=1, blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_delhivery_awb_numbers'


class ZzArchiveDownloadReport(models.Model):
    seller_id = models.IntegerField()
    report_name = models.CharField(max_length=255)
    report_type = models.CharField(max_length=255, blank=True, null=True)
    report_status = models.CharField(max_length=255)
    report_download_url = models.TextField(blank=True, null=True)
    extra_urls = models.TextField(blank=True, null=True)
    payload = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_download_report'


class ZzArchiveDtdcAwbNumbers(models.Model):
    awb_number = models.CharField(max_length=20)
    used = models.CharField(max_length=1)
    used_time = models.DateTimeField(blank=True, null=True)
    used_by = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    seller_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_dtdc_awb_numbers'


class ZzArchiveEcomExpressAwbs(models.Model):
    courier_partner = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    awb_number = models.CharField(max_length=30)
    used = models.CharField(max_length=1)
    used_by = models.IntegerField()
    used_time = models.DateTimeField(blank=True, null=True)
    generated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zz_archive_ecom_express_awbs'


class ZzArchiveEkartAwbNumbers(models.Model):
    number = models.CharField(max_length=10)
    used = models.CharField(max_length=1)
    awb_number = models.CharField(max_length=20, blank=True, null=True)
    courier_partner = models.CharField(max_length=255, blank=True, null=True)
    generated_id = models.IntegerField(blank=True, null=True)
    generated = models.DateTimeField(blank=True, null=True)
    assigned = models.CharField(max_length=255, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    used_by = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zz_archive_ekart_awb_numbers'


class ZzArchiveEmployeeWorkLogs(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    operation = models.CharField(max_length=6, blank=True, null=True)
    inserted = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zz_archive_employee_work_logs'


class ZzArchiveFileUploadJobLog(models.Model):
    job_id = models.IntegerField()
    awb_number = models.CharField(max_length=255)
    weight = models.CharField(max_length=255, blank=True, null=True)
    length = models.CharField(max_length=255, blank=True, null=True)
    breadth = models.CharField(max_length=255, blank=True, null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    cod_transactions_id = models.CharField(max_length=255, blank=True, null=True)
    crf_id = models.CharField(max_length=255, blank=True, null=True)
    cod_amount = models.CharField(max_length=255, blank=True, null=True)
    remittance_amount = models.CharField(max_length=255, blank=True, null=True)
    utr_number = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_file_upload_job_log'


class ZzArchiveManifest(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    courier = models.CharField(max_length=50, blank=True, null=True)
    number_of_order = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    warehouse_name = models.TextField(blank=True, null=True)
    warehouse_address = models.TextField(blank=True, null=True)
    warehouse_contact = models.CharField(max_length=15, blank=True, null=True)
    warehouse_gst_no = models.CharField(max_length=20, blank=True, null=True)
    p_ref_no = models.CharField(max_length=30, blank=True, null=True)
    created = models.DateField(blank=True, null=True)
    created_time = models.TimeField(blank=True, null=True)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'zz_archive_manifest'


class ZzArchiveManifestOrder(models.Model):
    manifest_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_manifest_order'


class ZzArchiveMarutiAwbs(models.Model):
    courier_partner = models.CharField(max_length=50)
    awb_number = models.CharField(max_length=30)
    used = models.CharField(max_length=1)
    used_by = models.IntegerField(blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    assigned = models.CharField(max_length=1, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    generated_id = models.IntegerField(blank=True, null=True)
    generated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_maruti_awbs'


class ZzArchiveMarutiAwbsEcom(models.Model):
    courier_partner = models.CharField(max_length=50)
    awb_number = models.CharField(max_length=30)
    used = models.CharField(max_length=1)
    used_by = models.IntegerField(blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    assigned = models.CharField(max_length=1, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    generated_id = models.IntegerField(blank=True, null=True)
    generated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_maruti_awbs_ecom'


class ZzArchiveMpsAwbNumber(models.Model):
    order_id = models.IntegerField()
    awb_number = models.CharField(max_length=250)
    inserted = models.DateTimeField(blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    awb_barcode = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_mps_awb_number'


class ZzArchiveNdrAttempts(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    raised_date = models.TextField(blank=True, null=True)
    raised_time = models.TimeField(blank=True, null=True)
    action_by = models.CharField(max_length=50, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    action_date = models.TextField(blank=True, null=True)
    action_status = models.CharField(max_length=50, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    u_address_line1 = models.TextField(blank=True, null=True)
    u_address_line2 = models.TextField(blank=True, null=True)
    updated_mobile = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_ndr_attempts'


class ZzArchiveNotifications(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    type = models.CharField(max_length=255)
    notifiable_type = models.CharField(max_length=255)
    notifiable_id = models.PositiveBigIntegerField()
    data = models.TextField()
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_notifications'


class ZzArchiveOrderSmsLogs(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    awb_number = models.CharField(max_length=30, blank=True, null=True)
    order_status = models.CharField(max_length=20, blank=True, null=True)
    sent = models.CharField(max_length=1, blank=True, null=True)
    sent_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_order_sms_logs'


class ZzArchiveOrderTracking(models.Model):
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    status_code = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    status_description = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    updated_date = models.TextField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_order_tracking'


class ZzArchiveOrders(models.Model):
    order_number = models.CharField(max_length=30, blank=True, null=True)
    customer_order_number = models.CharField(max_length=30)
    seller_id = models.IntegerField(blank=True, null=True)
    warehouse_id = models.IntegerField(blank=True, null=True)
    order_type = models.CharField(max_length=50, blank=True, null=True)
    o_type = models.CharField(max_length=10, blank=True, null=True)
    b_customer_name = models.TextField(blank=True, null=True)
    b_customer_email = models.TextField(blank=True, null=True)
    b_address_line1 = models.TextField(blank=True, null=True)
    b_address_line2 = models.TextField(blank=True, null=True)
    b_country = models.CharField(max_length=40, blank=True, null=True)
    b_state = models.CharField(max_length=40, blank=True, null=True)
    b_city = models.CharField(max_length=40, blank=True, null=True)
    b_pincode = models.CharField(max_length=10, blank=True, null=True)
    b_contact = models.CharField(max_length=15, blank=True, null=True)
    b_contact_code = models.CharField(max_length=5, blank=True, null=True)
    p_warehouse_name = models.TextField(blank=True, null=True)
    p_customer_name = models.TextField(blank=True, null=True)
    p_address_line1 = models.TextField(blank=True, null=True)
    p_address_line2 = models.TextField(blank=True, null=True)
    p_country = models.CharField(max_length=50, blank=True, null=True)
    p_state = models.CharField(max_length=50, blank=True, null=True)
    p_city = models.CharField(max_length=50, blank=True, null=True)
    p_pincode = models.CharField(max_length=10, blank=True, null=True)
    p_contact = models.CharField(max_length=15, blank=True, null=True)
    p_contact_code = models.CharField(max_length=5, blank=True, null=True)
    s_customer_name = models.TextField(blank=True, null=True)
    s_address_line1 = models.TextField(blank=True, null=True)
    s_address_line2 = models.TextField(blank=True, null=True)
    s_country = models.CharField(max_length=50, blank=True, null=True)
    s_state = models.CharField(max_length=50, blank=True, null=True)
    s_city = models.CharField(max_length=50, blank=True, null=True)
    s_pincode = models.CharField(max_length=10, blank=True, null=True)
    s_contact = models.CharField(max_length=15, blank=True, null=True)
    s_contact_code = models.CharField(max_length=5, blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)
    length = models.CharField(max_length=20, blank=True, null=True)
    breadth = models.CharField(max_length=20, blank=True, null=True)
    height = models.CharField(max_length=20, blank=True, null=True)
    vol_weight = models.FloatField()
    c_weight = models.IntegerField(blank=True, null=True)
    c_length = models.IntegerField(blank=True, null=True)
    c_breadth = models.IntegerField(blank=True, null=True)
    c_height = models.IntegerField(blank=True, null=True)
    s_charge = models.CharField(max_length=10, blank=True, null=True)
    c_charge = models.CharField(max_length=10, blank=True, null=True)
    shipping_charges = models.FloatField(blank=True, null=True)
    cod_charges = models.FloatField(blank=True, null=True)
    cod_maintenence = models.FloatField(blank=True, null=True)
    rto_charges = models.CharField(max_length=10, blank=True, null=True)
    total_charges = models.CharField(max_length=10, blank=True, null=True)
    early_cod_charges = models.FloatField(blank=True, null=True)
    gst_charges = models.FloatField(blank=True, null=True)
    excess_weight_charges = models.CharField(max_length=10, blank=True, null=True)
    discount = models.CharField(max_length=10, blank=True, null=True)
    invoice_amount = models.CharField(max_length=10, blank=True, null=True)
    cgst = models.FloatField(blank=True, null=True)
    sgst = models.FloatField(blank=True, null=True)
    igst = models.FloatField(blank=True, null=True)
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    alternate_awb_number = models.CharField(max_length=30, blank=True, null=True)
    xb_token_number = models.CharField(max_length=50, blank=True, null=True)
    awb_assigned_date = models.DateTimeField(blank=True, null=True)
    awb_barcode = models.TextField(blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    inserted_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    product_sku = models.TextField(blank=True, null=True)
    pickup_address = models.TextField(blank=True, null=True)
    delivery_address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50)
    delivery_stutus = models.CharField(max_length=50, blank=True, null=True)
    escalation_status = models.CharField(max_length=50, blank=True, null=True)
    ndr_action = models.CharField(max_length=50, blank=True, null=True)
    ndr_status = models.CharField(max_length=50, blank=True, null=True)
    rto_status = models.CharField(max_length=20, blank=True, null=True)
    pickup_time = models.CharField(max_length=50, blank=True, null=True)
    pickup_done = models.CharField(max_length=10, blank=True, null=True)
    pickup_schedule = models.CharField(max_length=1, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    manifest_status = models.CharField(max_length=1, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    reason_for_cancel = models.TextField(blank=True, null=True)
    reason_for_ndr = models.TextField(blank=True, null=True)
    reason_for_delay = models.TextField(blank=True, null=True)
    orderno_barcode = models.TextField(blank=True, null=True)
    zone = models.CharField(max_length=5, blank=True, null=True)
    invoice_status = models.CharField(max_length=1)
    delivered_date = models.DateTimeField(blank=True, null=True)
    expected_delivery_date = models.DateField(blank=True, null=True)
    last_sync = models.DateTimeField()
    ndr_status_date = models.CharField(max_length=50, blank=True, null=True)
    cod_remmited = models.CharField(max_length=1)
    reseller_name = models.CharField(max_length=50, blank=True, null=True)
    weight_disputed = models.CharField(max_length=1)
    settled_weight_disputed = models.CharField(max_length=1, blank=True, null=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    last_verified = models.DateTimeField(blank=True, null=True)
    fulfillment_id = models.CharField(max_length=50, blank=True, null=True)
    location_id = models.CharField(max_length=50, blank=True, null=True)
    seller_channel_id = models.IntegerField(blank=True, null=True)
    seller_channel_name = models.CharField(max_length=255, blank=True, null=True)
    suggested_awb = models.CharField(max_length=100, blank=True, null=True)
    reference_code = models.TextField(blank=True, null=True)
    marketplace = models.TextField(blank=True, null=True)
    marketplace_id = models.TextField(blank=True, null=True)
    amazon_order_id = models.IntegerField(blank=True, null=True)
    manifest_sent = models.CharField(max_length=1, blank=True, null=True)
    product_qty = models.IntegerField()
    fulfillment_sent = models.CharField(max_length=1)
    imported = models.DateTimeField(blank=True, null=True)
    weight_updated = models.CharField(max_length=1, blank=True, null=True)
    amazon_shipment_id = models.CharField(max_length=200, blank=True, null=True)
    amazon_label = models.TextField(blank=True, null=True)
    shipment_type = models.CharField(max_length=10, blank=True, null=True)
    number_of_packets = models.IntegerField(blank=True, null=True)
    is_master = models.CharField(max_length=10, blank=True, null=True)
    parent_id = models.PositiveBigIntegerField(blank=True, null=True)
    master_id = models.TextField(blank=True, null=True)
    bluedart_label = models.TextField(blank=True, null=True)
    route_code = models.CharField(max_length=100, blank=True, null=True)
    ewaybill_number = models.CharField(max_length=50, blank=True, null=True)
    shipping_partner = models.CharField(max_length=25, blank=True, null=True)
    ndr_raised_time = models.DateTimeField(blank=True, null=True)
    seller_order_type = models.CharField(max_length=3)
    last_executed = models.DateTimeField(blank=True, null=True)
    gati_ou_code = models.CharField(max_length=255, blank=True, null=True)
    gati_package_no = models.CharField(max_length=255, blank=True, null=True)
    is_tagged = models.CharField(max_length=1, blank=True, null=True)
    global_type = models.CharField(max_length=30)
    same_as_rto = models.CharField(max_length=1, blank=True, null=True)
    rto_warehouse_id = models.IntegerField(blank=True, null=True)
    ondc_seller_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_orders'


class ZzArchivePickedOrdersList(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    from_status = models.CharField(max_length=30, blank=True, null=True)
    to_status = models.CharField(max_length=30, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_picked_orders_list'


class ZzArchiveProducts(models.Model):
    order_id = models.IntegerField()
    product_sku = models.TextField(blank=True, null=True)
    product_name = models.TextField()
    product_unitprice = models.CharField(max_length=10, blank=True, null=True)
    product_qty = models.CharField(max_length=10, blank=True, null=True)
    total_amount = models.CharField(max_length=10, blank=True, null=True)
    item_id = models.CharField(max_length=50)
    invoice_reference_number = models.CharField(max_length=60, blank=True, null=True)
    export_reference_number = models.CharField(max_length=60, blank=True, null=True)
    hsn_number = models.CharField(max_length=50, blank=True, null=True)
    hts_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_products'


class ZzArchiveTransactions(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField()
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
        db_table = 'zz_archive_transactions'


class ZzArchiveWeightReconciliation(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    e_weight = models.FloatField(blank=True, null=True)
    e_length = models.FloatField(blank=True, null=True)
    e_breadth = models.FloatField(blank=True, null=True)
    e_height = models.FloatField(blank=True, null=True)
    applied_amount = models.FloatField(blank=True, null=True)
    c_weight = models.FloatField(blank=True, null=True)
    c_length = models.FloatField(blank=True, null=True)
    c_breadth = models.FloatField(blank=True, null=True)
    c_height = models.FloatField(blank=True, null=True)
    charged_amount = models.FloatField(blank=True, null=True)
    s_weight = models.FloatField(blank=True, null=True)
    s_length = models.FloatField(blank=True, null=True)
    s_breadth = models.FloatField(blank=True, null=True)
    s_height = models.FloatField(blank=True, null=True)
    settled_amount = models.FloatField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    action_taken_by = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    display_status = models.CharField(max_length=1, blank=True, null=True)
    is_error = models.CharField(max_length=25, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_weight_reconciliation'


class ZzArchiveXbeesAwbNumbers(models.Model):
    order_type = models.CharField(max_length=10, blank=True, null=True)
    batch_number = models.CharField(max_length=20, blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    used = models.CharField(max_length=1, blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    assigned = models.CharField(max_length=1, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    generated_id = models.IntegerField(blank=True, null=True)
    generated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_xbees_awb_numbers'


class ZzArchiveXbeesAwbNumbersUnique(models.Model):
    order_type = models.CharField(max_length=10, blank=True, null=True)
    batch_number = models.CharField(max_length=20, blank=True, null=True)
    awb_number = models.CharField(max_length=50, blank=True, null=True)
    used = models.CharField(max_length=1, blank=True, null=True)
    used_time = models.DateTimeField(blank=True, null=True)
    courier_partner = models.CharField(max_length=50, blank=True, null=True)
    assigned = models.CharField(max_length=1, blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    generated_id = models.IntegerField(blank=True, null=True)
    generated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_archive_xbees_awb_numbers_unique'


class ZzChannelsDeleted(models.Model):
    id = models.IntegerField(primary_key=True)
    seller_id = models.IntegerField()
    channel_name = models.CharField(max_length=100, blank=True, null=True)
    channel = models.CharField(max_length=100, blank=True, null=True)
    api_key = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    store_url = models.TextField(blank=True, null=True)
    shared_secret = models.TextField(blank=True, null=True)
    woo_consumer_key = models.TextField(blank=True, null=True)
    woo_consumer_secret = models.TextField(blank=True, null=True)
    magento_access_token = models.TextField(blank=True, null=True)
    store_hippo_access_key = models.TextField(blank=True, null=True)
    kart_rocket_api_key = models.TextField(blank=True, null=True)
    auto_fulfill = models.CharField(max_length=1, blank=True, null=True)
    auto_cancel = models.CharField(max_length=1, blank=True, null=True)
    auto_cod_paid = models.CharField(max_length=1, blank=True, null=True)
    last_sync = models.DateTimeField(blank=True, null=True)
    last_id = models.CharField(max_length=20, blank=True, null=True)
    amazon_mws_token = models.CharField(max_length=200, blank=True, null=True)
    amazon_seller_id = models.CharField(max_length=200, blank=True, null=True)
    company_id = models.CharField(max_length=100, blank=True, null=True)
    company_token = models.CharField(max_length=100, blank=True, null=True)
    amazon_token = models.TextField(blank=True, null=True)
    company_carrier_id = models.CharField(max_length=50, blank=True, null=True)
    last_executed = models.DateTimeField(blank=True, null=True)
    amazon_refresh_token = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    amazon_report_id = models.TextField(blank=True, null=True)
    fetch_woocommerce_order_number = models.CharField(max_length=1, blank=True, null=True)
    scince_abandon_id = models.CharField(max_length=255, blank=True, null=True)
    send_abandon_sms = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_channels_deleted'


class ZzTrackingExceptionLog(models.Model):
    order_id = models.IntegerField()
    awb_number = models.CharField(max_length=20)
    exception_message = models.TextField()
    inserted = models.DateTimeField()
    seller_id = models.IntegerField(blank=True, null=True)
    courier_partner = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_tracking_exception_log'
