# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190509_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='PreRequisite',
            field=models.BinaryField(default=False),
        ),
    ]
