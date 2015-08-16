# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp_game', '0003_auto_20150816_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.IntegerField(),
        ),
    ]
