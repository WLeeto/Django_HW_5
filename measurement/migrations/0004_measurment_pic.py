# Generated by Django 4.1.3 on 2022-12-13 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_remove_sensor_measure_measurment_sensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurment',
            name='pic',
            field=models.ImageField(null=True, upload_to='pics/'),
        ),
    ]
