# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 13:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_normalpost_secondtitle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='normalpost',
            options={'ordering': ['-Timestamp', '-Updated']},
        ),
    ]
