# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0007_auto_20190108_0158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='country',
            new_name='city',
        ),
    ]
