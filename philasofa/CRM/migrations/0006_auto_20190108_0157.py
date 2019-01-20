# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0005_auto_20190108_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order_cost',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_No',
            field=models.IntegerField(),
        ),
    ]
