# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-27 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20190127_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(),
        ),
    ]
