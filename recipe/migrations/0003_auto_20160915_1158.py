# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-15 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20160915_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
