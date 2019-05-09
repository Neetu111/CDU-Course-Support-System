# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190419_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='Semester',
        ),
        migrations.AddField(
            model_name='coursemajor',
            name='Semester',
            field=models.DecimalField(default=1, max_digits=1, decimal_places=0),
            preserve_default=False,
        ),
    ]
