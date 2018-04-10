# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-04 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Home.Kid')),
            ],
        ),
    ]
