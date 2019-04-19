# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseMajor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('CourseCode', models.CharField(max_length=10)),
                ('Field', models.CharField(max_length=400)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='Field',
        ),
        migrations.AddField(
            model_name='course',
            name='CourseType',
            field=models.CharField(max_length=100, default='Undergraduate'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='coursemajor',
            unique_together=set([('CourseCode', 'Field')]),
        ),
    ]
