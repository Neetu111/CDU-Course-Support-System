# Generated by Django 2.1 on 2019-05-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_merge_20190519_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='PreRequisite',
            field=models.BooleanField(default=False),
        ),
    ]
