# Generated by Django 5.0.4 on 2024-04-24 05:57

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_userupdate_balanc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userupdate',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, region=None, verbose_name='Contact phone number'),
        ),
        migrations.AlterField(
            model_name='userupdate',
            name='type_of_account',
            field=models.CharField(choices=[('Продавец', 'seller'), ('Покупатель', 'worker')], default=('Покупатель', 'worker')),
        ),
    ]
