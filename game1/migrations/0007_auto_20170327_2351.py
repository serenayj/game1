# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game1', '0006_auto_20170327_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='hid',
            name='username',
            field=models.CharField(default=b'someone', max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default=b'someone', max_length=140),
        ),
    ]
