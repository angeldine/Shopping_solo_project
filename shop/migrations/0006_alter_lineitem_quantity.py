# Generated by Django 4.1.7 on 2023-05-01 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_cart_id_alter_lineitem_id_alter_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
