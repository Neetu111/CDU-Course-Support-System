# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190514_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='PreRequisite',
            field=models.BooleanField(default=False),
        ),
    ]
