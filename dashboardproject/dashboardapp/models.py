from django.db import models

# Create your models here. parent

class Parentsidebar(models.Model):
    p_name = models.CharField(max_length=100,null=True,blank=True)
    # created_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.p_name

class Childsidebar(models.Model):
    c_name = models.CharField(max_length=100,null=True,blank=True)
    # created_at = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.Childsidebar
    
class Shipmenttype(models.Model):
    shipment_name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.shipment_name

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
    inserted = models.DateTimeField(auto_now=True,blank=True, null=True)
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



class Products(models.Model):
    order_id = models.IntegerField()
    product_sku = models.TextField(blank=True, null=True)
    product_name = models.TextField()
    product_unitprice = models.CharField(max_length=10, blank=True, null=True)
    product_qty = models.CharField(max_length=10, blank=True, null=True)
    total_amount = models.CharField(max_length=10, blank=True, null=True)
    item_id = models.CharField(max_length=50,blank=True,null=True)
    invoice_reference_number = models.CharField(max_length=60, blank=True, null=True)
    export_reference_number = models.CharField(max_length=60, blank=True, null=True)
    hsn_number = models.CharField(max_length=50, blank=True, null=True)
    hts_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'