# Generated by Django 3.0.8 on 2020-08-10 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_addresses', '0001_initial'),
        ('orders', '0002_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping_addresses.ShippingAddress'),
        ),
    ]
