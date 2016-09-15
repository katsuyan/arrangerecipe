# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-15 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='味付け')),
            ],
        ),
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='recipe.Category', verbose_name='カテゴリー')),
            ],
        ),
        migrations.CreateModel(
            name='Taste',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='味付け')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='taste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='recipe.Taste', verbose_name='味付け'),
        ),
    ]
