# Generated by Django 3.0.8 on 2020-07-22 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_auto_20200721_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='concurrency',
            field=models.IntegerField(default=1),
        ),
    ]