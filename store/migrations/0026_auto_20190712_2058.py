# Generated by Django 2.2.2 on 2019-07-12 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20190712_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='number',
            field=models.IntegerField(blank=True, default=20, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
