# Generated by Django 2.0.3 on 2019-05-23 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_unit_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemajor',
            name='Year',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=1),
            preserve_default=False,
        ),
    ]
