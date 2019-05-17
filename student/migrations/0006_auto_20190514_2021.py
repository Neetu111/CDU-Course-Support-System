# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20190514_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='CourseCode',
            field=models.SlugField(primary_key=True, max_length=10, serialize=False),
        ),
    ]
