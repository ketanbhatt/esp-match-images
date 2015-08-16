# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp_game', '0002_game_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='player',
            new_name='players',
        ),
    ]
