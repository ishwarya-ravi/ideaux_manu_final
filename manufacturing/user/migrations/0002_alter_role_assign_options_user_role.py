# Generated by Django 4.1.4 on 2023-01-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role_assign',
            options={'permissions': (('staff', 'staff'), ('admin', 'admin'), ('user', 'user'), ('customer', 'customer'), ('employee', 'employee'))},
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Employee', 'Employee'), ('Customer', 'Customer'), ('Admin', 'Admin')], max_length=70, null=True),
        ),
    ]
