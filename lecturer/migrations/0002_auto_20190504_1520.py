# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='id',
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='LecturerID',
            field=models.CharField(primary_key=True, max_length=10, serialize=False),
        ),
    ]
