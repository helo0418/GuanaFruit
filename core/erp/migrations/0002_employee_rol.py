# Generated by Django 3.0.4 on 2022-08-17 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='rol',
            field=models.TextField(default=2, verbose_name='Rol'),
            preserve_default=False,
        ),
    ]
