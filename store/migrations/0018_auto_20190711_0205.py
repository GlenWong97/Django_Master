# Generated by Django 2.2.2 on 2019-07-10 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_question_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='index',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
