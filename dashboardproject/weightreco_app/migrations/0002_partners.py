# Generated by Django 5.0 on 2024-01-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weightreco_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.IntegerField()),
                ('title', models.CharField(max_length=60)),
                ('keyword', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('api_key', models.TextField(blank=True, null=True)),
                ('other_key', models.TextField(blank=True, null=True)),
                ('ship_url', models.TextField(blank=True, null=True)),
                ('track_url', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('weight_initial', models.IntegerField()),
                ('extra_limit', models.IntegerField()),
                ('serviceability_check', models.CharField(blank=True, max_length=50, null=True)),
                ('zone_a', models.IntegerField()),
                ('zone_b', models.IntegerField()),
                ('zone_c', models.IntegerField()),
                ('zone_d', models.IntegerField()),
                ('zone_e', models.IntegerField()),
                ('mps_enabled', models.CharField(blank=True, max_length=10, null=True)),
                ('reverse_enabled', models.CharField(blank=True, max_length=25, null=True)),
                ('liability_amount', models.FloatField(blank=True, null=True)),
                ('weight_category', models.CharField(blank=True, max_length=20, null=True)),
                ('international_enabled', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'partners',
                'managed': False,
            },
        ),
    ]
