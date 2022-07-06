# Generated by Django 4.0.4 on 2022-07-06 19:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0007_alter_cart_cart_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'ordering': ['cart', '-date_added']},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={},
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cart_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='client',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='date_added',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='client',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(default='Pending', max_length=255),
        ),
        migrations.AlterField(
            model_name='cart',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.client'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(max_length=255),
        ),
    ]
