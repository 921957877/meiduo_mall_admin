# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-22 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_address_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
