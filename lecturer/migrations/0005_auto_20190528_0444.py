# Generated by Django 2.1 on 2019-05-27 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0004_remove_lecturer_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='Name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]