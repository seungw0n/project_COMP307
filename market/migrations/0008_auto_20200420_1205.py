# Generated by Django 3.0.4 on 2020-04-20 12:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0007_auto_20200420_1130'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderProduct',
            new_name='OrderItem',
        ),
    ]