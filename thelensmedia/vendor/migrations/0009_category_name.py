# Generated by Django 4.1.3 on 2022-11-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_remove_product_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='undefined', max_length=100),
        ),
    ]