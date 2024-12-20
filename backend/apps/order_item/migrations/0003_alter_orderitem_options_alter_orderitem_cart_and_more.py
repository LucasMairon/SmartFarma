# Generated by Django 5.1.1 on 2024-10-21 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('order_item', '0002_remove_orderitem_price_alter_orderitem_cart'),
        ('product', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Order_Item', 'verbose_name_plural': 'Order_Items'},
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='cart.cart'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
