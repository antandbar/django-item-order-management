# Generated by Django 4.2.16 on 2024-09-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_order_total_price_excl_tax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='applicable_tax',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
