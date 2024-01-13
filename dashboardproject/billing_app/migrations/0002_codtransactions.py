# Generated by Django 5.0 on 2024-01-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True)),
                ('seller_id', models.IntegerField(blank=True, null=True)),
                ('crf_id', models.CharField(blank=True, max_length=10, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=1, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('redeem_type', models.CharField(blank=True, max_length=1, null=True)),
                ('utr_number', models.CharField(blank=True, max_length=30, null=True)),
                ('early_cod_charge', models.IntegerField(blank=True, null=True)),
                ('pay_type', models.CharField(blank=True, max_length=10, null=True)),
                ('remitted_by', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'cod_transactions',
                'managed': False,
            },
        ),
    ]