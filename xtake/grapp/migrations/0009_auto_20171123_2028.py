# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 20:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grapp', '0008_election_ko_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='selected_promise',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='shown_promise',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserResponse',
        ),
    ]