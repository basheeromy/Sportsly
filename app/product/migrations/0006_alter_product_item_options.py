# Generated by Django 4.2.4 on 2023-08-08 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_image_product_image_category_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_item',
            options={'ordering': ('-updated_on',)},
        ),
    ]
