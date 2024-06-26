# Generated by Django 4.2.9 on 2024-01-31 11:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_status', models.CharField(max_length=250)),
                ('payment_mode', models.CharField(choices=[('COD', 'Cash On Delivery'), ('CC', 'Credit Card'), ('DC', 'Debit Card'), ('UPI', 'Unified Payment Interface'), ('NB', 'Net Banking')], max_length=3)),
                ('payment_status', models.CharField(max_length=200)),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.billingaddress')),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_delete', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem_set', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product_item')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
