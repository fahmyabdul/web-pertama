# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 07:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0005_login_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_log',
            name='log_action',
        ),
    ]
