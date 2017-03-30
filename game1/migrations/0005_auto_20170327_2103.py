# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game1', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pairs',
            fields=[
                ('pairid', models.AutoField(primary_key=True, serialize=False)),
                ('channelid', models.CharField(max_length=128, unique=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userid',
            field=models.ForeignKey(db_column=b'turkid', on_delete=django.db.models.deletion.CASCADE, to='game1.HID'),
        ),
        migrations.AddField(
            model_name='pairs',
            name='user1id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userid1', to='game1.UserProfile'),
        ),
        migrations.AddField(
            model_name='pairs',
            name='user2id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userid2', to='game1.UserProfile'),
        ),
    ]