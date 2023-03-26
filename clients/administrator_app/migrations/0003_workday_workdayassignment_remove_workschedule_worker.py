# Generated by Django 4.0.3 on 2023-03-26 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator_app', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkDayAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='workschedule',
            name='worker',
        ),
    ]
