# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-29 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_boxsignout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxsignout',
            name='box_num',
            field=models.CharField(default='None', max_length=40),
        ),
    ]
