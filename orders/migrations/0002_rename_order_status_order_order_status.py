# Generated by Django 4.2.15 on 2024-08-16 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ORDER_STATUS',
            new_name='order_status',
        ),
    ]
