# Generated by Django 3.0.8 on 2020-08-12 04:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HospiHomes', '0004_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='cat',
            field=models.CharField(default=django.utils.timezone.now, max_length=6400),
            preserve_default=False,
        ),
    ]
