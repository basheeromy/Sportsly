# Generated by Django 4.2.9 on 2024-04-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Men'), ('W', 'Women')], max_length=10, null=True),
        ),
    ]
