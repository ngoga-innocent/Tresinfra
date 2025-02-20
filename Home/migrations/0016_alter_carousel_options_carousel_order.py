# Generated by Django 5.1.4 on 2025-02-20 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_alter_carousel_options_team_management_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ['order', 'created_at']},
        ),
        migrations.AddField(
            model_name='carousel',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
