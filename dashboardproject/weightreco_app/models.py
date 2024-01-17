from django.db import models


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
