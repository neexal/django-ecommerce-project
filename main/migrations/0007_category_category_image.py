# Generated by Django 3.0 on 2020-11-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201112_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
