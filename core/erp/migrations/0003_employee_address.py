# Generated by Django 3.0.4 on 2022-08-17 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_employee_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.TextField(default=2, verbose_name='Direccion'),
            preserve_default=False,
        ),
    ]
