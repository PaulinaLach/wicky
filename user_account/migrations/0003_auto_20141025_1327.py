# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0002_auto_20141025_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='images/avatar/'),
        ),
    ]
