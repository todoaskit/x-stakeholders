# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_auto_20171206_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='marriage',
            field=models.IntegerField(choices=[(None, '선택해주세요'), (0, '기혼'), (1, '사별'), (2, '이혼'), (3, '별거'), (4, '미혼'), (5, '동거')], default=1, verbose_name='결혼 상태'),
            preserve_default=False,
        ),
    ]
