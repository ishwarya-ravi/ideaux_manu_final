# Generated by Django 4.1.5 on 2023-01-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manu', '0018_product_raw_material_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sell_quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sell_status',
            field=models.CharField(blank=True, choices=[('profit', 'profit'), ('loss', 'loss')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sell_status_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=16, null=True),
        ),
    ]
