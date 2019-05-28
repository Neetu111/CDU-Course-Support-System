# Generated by Django 2.1 on 2019-05-27 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0006_auto_20190528_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='LecturerID',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='Name',
            field=models.OneToOneField(default='CDU', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
