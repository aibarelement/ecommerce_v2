# Generated by Django 4.1.5 on 2023-02-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerproduct',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
