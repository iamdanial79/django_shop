# Generated by Django 3.2.8 on 2021-10-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer_perc',
            field=models.FloatField(default=0.0),
        ),
    ]
