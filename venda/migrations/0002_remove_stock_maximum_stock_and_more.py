# Generated by Django 5.0.4 on 2024-06-25 17:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='maximum_stock',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='minimum_stock',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_cate', to='venda.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
