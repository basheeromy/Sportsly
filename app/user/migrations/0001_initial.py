# Generated by Django 4.2.4 on 2023-09-03 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('company_name', models.CharField(blank=True, max_length=250, null=True)),
                ('apartment', models.CharField(blank=True, max_length=250, null=True)),
                ('street', models.CharField(max_length=300)),
                ('town', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('pin', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=15)),
                ('secondary_mob', models.CharField(max_length=15)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
