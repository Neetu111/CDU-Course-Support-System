# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20190514_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='CourseCode',
            field=models.CharField(primary_key=True, max_length=10, serialize=False),
        ),
    ]
