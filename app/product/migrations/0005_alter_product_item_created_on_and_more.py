# Generated by Django 4.2.5 on 2023-09-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_item_color_alter_product_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_item',
            name='created_on',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='product_item',
            name='updated_on',
            field=models.DateTimeField(editable=False),
        ),
    ]
