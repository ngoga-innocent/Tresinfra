# Generated by Django 5.1.4 on 2025-01-13 15:55

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
