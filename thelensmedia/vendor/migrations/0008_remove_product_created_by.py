# Generated by Django 4.1.3 on 2022-11-26 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_alter_product_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_by',
        ),
    ]
