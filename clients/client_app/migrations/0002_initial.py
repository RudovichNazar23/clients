# Generated by Django 4.1.3 on 2022-12-03 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client_app', '0001_initial'),
        ('worker_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Worker', to='worker_app.worker'),
        ),
    ]
