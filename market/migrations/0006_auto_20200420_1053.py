# Generated by Django 3.0.4 on 2020-04-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
