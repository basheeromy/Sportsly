# Generated by Django 4.2.5 on 2023-09-13 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_item_color_alter_product_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_item',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.color'),
        ),
        migrations.AlterField(
            model_name='product_item',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productitem_set', to='product.product'),
        ),
        migrations.AlterField(
            model_name='product_item',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.size'),
        ),
    ]
