<<<<<<< HEAD
# Generated by Django 3.0.5 on 2020-04-19 14:57
=======
# Generated by Django 3.0.4 on 2020-04-19 15:17
>>>>>>> f9db38b0da6d50f9fb77c152043aec6969cbcdda

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0003_auto_20200419_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
<<<<<<< HEAD
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Product')),
                ('user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
=======
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Product')),
>>>>>>> f9db38b0da6d50f9fb77c152043aec6969cbcdda
            ],
        ),
    ]
