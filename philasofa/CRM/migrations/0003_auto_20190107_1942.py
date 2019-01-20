# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0002_inventory_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='holding_cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='inventory_quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='purchase_cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='purchase_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='selling_price',
            field=models.IntegerField(),
        ),
    ]
