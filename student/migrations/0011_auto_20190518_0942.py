# Generated by Django 2.1 on 2019-05-18 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20190518_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='PreRequisite',
            field=models.BooleanField(default=False),
        ),
    ]
