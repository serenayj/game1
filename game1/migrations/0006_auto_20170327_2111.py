# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game1', '0005_auto_20170327_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hid',
            name='id',
        ),
        migrations.AlterField(
            model_name='hid',
            name='turkid',
            field=models.CharField(max_length=128, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game1.HID'),
        ),
    ]
