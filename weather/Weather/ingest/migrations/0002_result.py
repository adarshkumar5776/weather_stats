# Generated by Django 3.2.16 on 2023-01-18 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('Max_temp', models.IntegerField()),
                ('Min_temp', models.IntegerField()),
                ('Precipitation', models.IntegerField()),
            ],
        ),
    ]
