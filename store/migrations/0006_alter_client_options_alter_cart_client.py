# Generated by Django 4.0.4 on 2022-06-12 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_cart_cart_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['client_id']},
        ),
        migrations.AlterField(
            model_name='cart',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.client'),
        ),
    ]
