# Generated by Django 3.0.8 on 2020-08-24 15:02

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_articlepost_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(upload_to='article/%Y%m%d'),
        ),
    ]