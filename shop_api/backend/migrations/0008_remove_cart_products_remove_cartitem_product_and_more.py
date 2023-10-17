# Generated by Django 4.2.5 on 2023-10-15 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_cart_products_alter_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='products_info',
            field=models.ManyToManyField(related_name='products', through='backend.CartItem', to='backend.productinfo'),
        ),
    ]
