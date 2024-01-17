# Generated by Django 5.0 on 2024-01-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeightReconciliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_id', models.IntegerField(blank=True, null=True)),
                ('awb_number', models.CharField(blank=True, max_length=50, null=True)),
                ('e_weight', models.FloatField(blank=True, null=True)),
                ('e_length', models.FloatField(blank=True, null=True)),
                ('e_breadth', models.FloatField(blank=True, null=True)),
                ('e_height', models.FloatField(blank=True, null=True)),
                ('applied_amount', models.FloatField(blank=True, null=True)),
                ('c_weight', models.FloatField(blank=True, null=True)),
                ('c_length', models.FloatField(blank=True, null=True)),
                ('c_breadth', models.FloatField(blank=True, null=True)),
                ('c_height', models.FloatField(blank=True, null=True)),
                ('charged_amount', models.FloatField(blank=True, null=True)),
                ('s_weight', models.FloatField(blank=True, null=True)),
                ('s_length', models.FloatField(blank=True, null=True)),
                ('s_breadth', models.FloatField(blank=True, null=True)),
                ('s_height', models.FloatField(blank=True, null=True)),
                ('settled_amount', models.FloatField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('action_taken_by', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('display_status', models.CharField(blank=True, max_length=1, null=True)),
                ('is_error', models.CharField(blank=True, max_length=25, null=True)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'weight_reconciliation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeightReconciliationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_reconciliation_id', models.IntegerField(blank=True, null=True)),
                ('action_taken_by', models.CharField(blank=True, max_length=50, null=True)),
                ('history_date', models.DateTimeField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'weight_reconciliation_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeightReconciliationImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_reconciliation_history_id', models.IntegerField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'weight_reconciliation_images',
                'managed': False,
            },
        ),
    ]