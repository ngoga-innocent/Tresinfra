# Generated by Django 5.1.4 on 2025-02-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_misconductreport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='team',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
