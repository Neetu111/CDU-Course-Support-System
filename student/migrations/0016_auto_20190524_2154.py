# Generated by Django 2.0.3 on 2019-05-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_auto_20190523_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='Semester',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='Year',
        ),
        migrations.AddField(
            model_name='semesterunit',
            name='Field',
            field=models.CharField(default='XENG01', max_length=400),
        ),
        migrations.AddField(
            model_name='semesterunit',
            name='Semester',
            field=models.IntegerField(choices=[(1, 1), (2, 2)], default=1),
        ),
        migrations.AddField(
            model_name='semesterunit',
            name='Year',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1),
        ),
        migrations.AlterUniqueTogether(
            name='semesterunit',
            unique_together={('UnitCode', 'CourseCode', 'Semester', 'Year', 'Field')},
        ),
    ]
