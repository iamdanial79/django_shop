# Generated by Django 3.2.2 on 2021-10-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20211025_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(default=None, upload_to='product_pic'),
        ),
    ]
