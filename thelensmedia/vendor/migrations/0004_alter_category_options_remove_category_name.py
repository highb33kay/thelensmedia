# Generated by Django 4.1.3 on 2022-11-26 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_category_productowner_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('Category',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
    ]