# Generated by Django 4.0.4 on 2022-06-08 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_cart_items_cart_cart_id_alter_client_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cart',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.client'),
        ),
    ]
