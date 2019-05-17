# Generated by Django 2.1 on 2019-05-15 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20190514_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemajor',
            name='CourseName',
            field=models.CharField(default='course', max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='CourseCode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='CourseName',
            field=models.CharField(max_length=400, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unit',
            name='UnitCode',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='unit',
            name='UnitName',
            field=models.CharField(max_length=400, primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='coursemajor',
            name='CourseCode',
        ),
        migrations.AlterUniqueTogether(
            name='coursemajor',
            unique_together={('CourseName', 'Field')},
        ),
    ]
