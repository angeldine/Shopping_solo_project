# Generated by Django 4.1.7 on 2023-05-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_order_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(max_length=200),
        ),
    ]
