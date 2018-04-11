# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-11 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_remove_signin_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signin',
            name='kid',
        ),
        migrations.AddField(
            model_name='signin',
            name='kid_grade',
            field=models.IntegerField(default=7),
        ),
        migrations.AddField(
            model_name='signin',
            name='kid_name',
            field=models.CharField(default='None', max_length=40),
        ),
    ]
