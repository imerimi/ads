# Generated by Django 5.0.2 on 2024-02-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_mainlocation_job_mainloc'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='mainlocation',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='mainloc',
            field=models.CharField(max_length=100),
        ),
    ]
