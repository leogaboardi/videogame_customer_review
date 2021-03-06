# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 01:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(default=1)),
                ('review', models.CharField(max_length=2000)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
            ],
        ),
    ]
