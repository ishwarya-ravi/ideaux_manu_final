# Generated by Django 4.1.5 on 2023-01-27 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manu', '0021_alter_product_quantity_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sub_amount',
        ),
    ]
