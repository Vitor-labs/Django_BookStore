# Generated by Django 4.0.4 on 2022-06-13 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_client_options_alter_cart_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
