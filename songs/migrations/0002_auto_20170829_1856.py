# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-29 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='song',
            name='composition_date',
            field=models.PositiveIntegerField(default=1900),
        ),
    ]
