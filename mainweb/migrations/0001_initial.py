# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bagian',
            fields=[
                ('bagian_id', models.AutoField(primary_key=True, serialize=False)),
                ('bagian_judul', models.CharField(max_length=200)),
                ('bagian_isi', models.TextField()),
            ],
        ),
    ]
