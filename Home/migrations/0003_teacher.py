# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-03 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20180322_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('techer_name', models.CharField(default='None', max_length=40)),
            ],
        ),
    ]