# Generated by Django 5.0.7 on 2024-11-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_address_secondary_mob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='tag',
            field=models.CharField(blank=True, choices=[('HOME', 'Home'), ('OFFICE', 'Office')], max_length=10, null=True),
        ),
    ]