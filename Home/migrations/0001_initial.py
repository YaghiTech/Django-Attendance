# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-22 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kid_first_name', models.CharField(default='None', max_length=20)),
                ('kid_last_name', models.CharField(default='None', max_length=20)),
                ('kid_grade', models.IntegerField(default=7, max_length=20)),
                ('kid_signed_in', models.BooleanField(default=False)),
            ],
        ),
    ]