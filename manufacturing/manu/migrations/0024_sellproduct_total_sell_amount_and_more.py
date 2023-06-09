# Generated by Django 4.1.5 on 2023-01-27 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manu', '0023_remove_product_sell_status_amount_product_sub_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellproduct',
            name='total_sell_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16),
        ),
        migrations.AlterField(
            model_name='manufacturing',
            name='charges_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16),
        ),
    ]
