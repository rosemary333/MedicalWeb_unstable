# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 08:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0012_auto_20170328_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachinfo',
            old_name='information',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='groupinfo',
            old_name='information',
            new_name='description',
        ),
    ]
