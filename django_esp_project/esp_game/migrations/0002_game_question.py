# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp_game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstPlayerChoice', models.IntegerField(null=True, blank=True)),
                ('game', models.ForeignKey(to='esp_game.Game')),
                ('primaryImage', models.ForeignKey(to='esp_game.PrimaryImage')),
                ('secondaryImage1', models.ForeignKey(related_name='choice1', blank=True, to='esp_game.SecondaryImage', null=True)),
                ('secondaryImage2', models.ForeignKey(related_name='choice2', blank=True, to='esp_game.SecondaryImage', null=True)),
                ('secondaryImage3', models.ForeignKey(related_name='choice3', blank=True, to='esp_game.SecondaryImage', null=True)),
            ],
        ),
    ]
