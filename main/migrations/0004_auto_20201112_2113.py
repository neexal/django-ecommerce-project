# Generated by Django 3.0 on 2020-11-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201112_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='main/images/'),
        ),
    ]
