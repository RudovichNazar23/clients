# Generated by Django 4.0.3 on 2022-12-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0004_remove_feedback_date_remove_feedback_feedback_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='not_registered_user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Must be unique'}, max_length=50, unique=True),
        ),
    ]
