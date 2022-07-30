# Generated by Django 4.0.4 on 2022-07-30 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('summary', models.TextField(default='Here some Text', max_length=1000)),
                ('pages', models.IntegerField(default=1)),
                ('rating', models.FloatField(default=0.0)),
                ('price', models.FloatField()),
                ('isbn', models.CharField(max_length=13)),
                ('publisher', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('genre', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
