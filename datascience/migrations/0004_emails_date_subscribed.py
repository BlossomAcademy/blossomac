# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-01 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('datascience', '0003_auto_20180801_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='emails',
            name='date_subscribed',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
