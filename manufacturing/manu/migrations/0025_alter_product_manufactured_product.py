# Generated by Django 4.1.5 on 2023-01-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manu', '0024_sellproduct_total_sell_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufactured_product',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
