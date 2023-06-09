# Generated by Django 4.1.5 on 2023-01-27 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manu', '0016_remove_sellproduct_total_sell_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturing',
            name='charges_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=16, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_charge_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_manufactured_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16),
        ),
    ]
