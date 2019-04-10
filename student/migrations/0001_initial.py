# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('CourseCode', models.CharField(primary_key=True, max_length=10, serialize=False)),
                ('CourseName', models.CharField(max_length=400)),
                ('Field', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PreRequisite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('UnitCode', models.CharField(max_length=6)),
                ('PreRequisiteCode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='SemesterUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('UnitCode', models.CharField(max_length=6)),
                ('CourseCode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('UnitCode', models.CharField(primary_key=True, max_length=6, serialize=False)),
                ('UnitName', models.CharField(max_length=400)),
                ('Type', models.CharField(max_length=2)),
                ('PreRequisite', models.BinaryField()),
                ('Semester', models.DecimalField(max_digits=1, decimal_places=0)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='semesterunit',
            unique_together=set([('UnitCode', 'CourseCode')]),
        ),
        migrations.AlterUniqueTogether(
            name='prerequisite',
            unique_together=set([('UnitCode', 'PreRequisiteCode')]),
        ),
    ]
