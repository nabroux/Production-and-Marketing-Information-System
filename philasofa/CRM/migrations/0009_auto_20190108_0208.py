# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0008_auto_20190108_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='order_cost',
            field=models.IntegerField(),
        ),
    ]
