# Generated by Django 5.0.1 on 2024-01-25 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_product_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_by',
        ),
    ]