# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20141024_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photograph',
            name='data',
            field=models.ImageField(upload_to='images/photos/'),
        ),
    ]
