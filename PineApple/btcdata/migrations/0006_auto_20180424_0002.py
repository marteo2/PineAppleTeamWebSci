# Generated by Django 2.0.2 on 2018-04-24 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btcdata', '0005_auto_20180423_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedata',
            name='time',
            field=models.DateTimeField(verbose_name='date get'),
        ),
    ]
