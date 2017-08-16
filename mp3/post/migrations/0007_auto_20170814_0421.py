# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20170812_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='mFrom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='post.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='mTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='post.User'),
        ),
    ]