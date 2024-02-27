# Generated by Django 5.0.2 on 2024-02-27 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('jobtype', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
                ('jd', models.CharField(max_length=10000)),
            ],
        ),
    ]