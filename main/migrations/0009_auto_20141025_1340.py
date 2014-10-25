# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20141025_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='user_account',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photograph',
            name='user_account',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
