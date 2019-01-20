# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0003_auto_20190107_1942'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Inventory',
            new_name='Product',
        ),
        migrations.AlterField(
            model_name='order',
            name='created_time',
            field=models.DateTimeField(),
        ),
    ]
