# Generated by Django 5.1.4 on 2025-01-11 15:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_ourservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourservice',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
