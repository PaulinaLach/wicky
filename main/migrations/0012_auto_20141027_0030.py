# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20141025_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photograph',
            name='albums',
            field=models.ManyToManyField(to='main.Album', blank=True),
        ),
        migrations.AlterField(
            model_name='photograph',
            name='category',
            field=models.ForeignKey(blank=True, to='main.Category'),
        ),
        migrations.AlterField(
            model_name='photograph',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='photograph',
            name='latitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='photograph',
            name='longitude',
            field=models.FloatField(blank=True),
        ),
    ]
