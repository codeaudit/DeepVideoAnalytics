# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-20 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0005_trainingset_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingset',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
