# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0004_auto_20190108_0143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='purchase_cost',
            new_name='order_time',
        ),
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
        migrations.AddField(
            model_name='order',
            name='order_No',
            field=models.IntegerField(default='0'),
        ),
    ]
