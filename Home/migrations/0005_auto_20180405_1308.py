# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-05 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_signin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signin',
            name='kid',
        ),
        migrations.AddField(
            model_name='signin',
            name='kid',
            field=models.ManyToManyField(to='Home.Kid'),
        ),
    ]
