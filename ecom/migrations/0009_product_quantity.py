# Generated by Django 4.2 on 2023-10-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=20),
            preserve_default=False,
        ),
    ]
