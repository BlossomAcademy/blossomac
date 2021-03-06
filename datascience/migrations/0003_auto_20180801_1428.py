# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-01 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datascience', '0002_aboutb_emailsb_faqsb_joinb_partnerb_privacyb_termsb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_addresses', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='AboutB',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='EmailsB',
        ),
        migrations.DeleteModel(
            name='FAQsB',
        ),
        migrations.DeleteModel(
            name='JoinB',
        ),
        migrations.DeleteModel(
            name='PartnerB',
        ),
        migrations.DeleteModel(
            name='PrivacyB',
        ),
        migrations.DeleteModel(
            name='TermsB',
        ),
    ]
