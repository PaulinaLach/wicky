# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_photograph_pluses'),
        ('user_account', '0003_auto_20141025_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='pluses',
            field=models.ManyToManyField(to='main.Photograph'),
            preserve_default=True,
        ),
    ]
