# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hitid', models.CharField(max_length=128, unique=True)),
                ('turkid', models.CharField(max_length=128, unique=True)),
                ('assid', models.CharField(max_length=128, unique=True)),
                ('provisional', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]