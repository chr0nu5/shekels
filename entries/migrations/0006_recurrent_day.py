# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-26 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0005_entry_recurrent'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurrent',
            name='day',
            field=models.IntegerField(default=1),
        ),
    ]