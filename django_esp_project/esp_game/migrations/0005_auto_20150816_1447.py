# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp_game', '0004_auto_20150816_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondaryimage',
            name='score',
            field=models.IntegerField(default=1),
        ),
    ]
