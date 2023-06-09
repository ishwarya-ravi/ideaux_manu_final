# Generated by Django 4.1.4 on 2023-01-28 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CRM', '0002_customer_created_at_customer_updated_at'),
        ('manu', '0030_sellproduct_is_active_sellproduct_status_sell'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('New', 'New'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Inprogress', 'Inprogress'), ('Completed', 'Completed')], default='New', max_length=160)),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('product_amount', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('customer', models.ForeignKey(max_length=190, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRM.customer')),
                ('product', models.ForeignKey(max_length=160, null=True, on_delete=django.db.models.deletion.CASCADE, to='manu.product')),
            ],
        ),
    ]
