# Generated by Django 4.2 on 2024-04-17 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]