# Generated by Django 2.1 on 2019-05-25 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0005_lecturer_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='upload',
        ),
    ]
