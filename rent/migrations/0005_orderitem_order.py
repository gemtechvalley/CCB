# Generated by Django 3.1.3 on 2021-01-07 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_order_orderitem_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rent.order'),
        ),
    ]
