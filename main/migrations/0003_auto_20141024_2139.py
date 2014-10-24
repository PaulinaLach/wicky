# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20141024_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photograph',
            name='data',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
