# Generated by Django 3.0.8 on 2020-08-12 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospiHomes', '0003_user1_hospis'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hn', models.CharField(max_length=64)),
                ('addr', models.CharField(max_length=6400)),
                ('specs', models.CharField(max_length=6400)),
                ('docts', models.CharField(max_length=6400)),
                ('conts', models.CharField(max_length=1000)),
                ('amb', models.CharField(max_length=64)),
            ],
        ),
    ]
