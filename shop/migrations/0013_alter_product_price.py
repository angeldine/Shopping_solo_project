# Generated by Django 4.1.7 on 2023-05-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_shippingaddress_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
