# Generated by Django 3.0.4 on 2022-09-15 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_auto_20220915_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale_product',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=19, verbose_name='Precio'),
        ),
    ]
