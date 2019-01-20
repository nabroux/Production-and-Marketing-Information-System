# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('customer_name', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
    ]
