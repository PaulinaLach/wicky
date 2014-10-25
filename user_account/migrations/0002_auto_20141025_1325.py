# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='about',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='avatar',
            field=models.ImageField(null=True, upload_to='images/avatar/'),
            preserve_default=True,
        ),
    ]
