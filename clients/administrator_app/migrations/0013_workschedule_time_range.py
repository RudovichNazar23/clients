# Generated by Django 4.0.3 on 2023-03-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator_app', '0012_timerange'),
    ]

    operations = [
        migrations.AddField(
            model_name='workschedule',
            name='time_range',
            field=models.CharField(choices=[], default='', max_length=500),
            preserve_default=False,
        ),
    ]
