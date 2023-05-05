# Generated by Django 4.0.3 on 2023-05-05 11:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator_app', '0007_remove_workday_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workdayassignment',
            name='workday',
            field=models.ForeignKey(choices=[(datetime.date(2023, 5, 7), datetime.date(2023, 5, 7)), (datetime.date(2023, 5, 15), datetime.date(2023, 5, 15))], on_delete=django.db.models.deletion.CASCADE, to='administrator_app.workday'),
        ),
    ]
