# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='profile',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]