# Generated by Django 4.1.4 on 2022-12-26 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.DateTimeField(),
        ),
    ]