# Generated by Django 5.1.1 on 2024-10-20 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('order_item', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='cart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='cart.cart'),
        ),
    ]
