# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('product_name', models.CharField(max_length=20)),
                ('purchase_price', models.IntegerField(max_length=10)),
                ('purchase_cost', models.IntegerField(max_length=10)),
                ('holding_cost', models.IntegerField(max_length=10)),
                ('selling_price', models.IntegerField(max_length=10)),
                ('inventory_quantity', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('quantity', models.IntegerField(max_length=10)),
                ('amount', models.IntegerField(max_length=10)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.ForeignKey(to='CRM.Customer')),
                ('product', models.ForeignKey(to='CRM.Inventory')),
            ],
        ),
    ]
