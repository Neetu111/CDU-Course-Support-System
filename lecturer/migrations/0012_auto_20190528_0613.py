# Generated by Django 2.1 on 2019-05-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0011_auto_20190528_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='id',
            field=models.AutoField(auto_created=True, default=56, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='LecturerID',
            field=models.CharField(max_length=10),
        ),
    ]
