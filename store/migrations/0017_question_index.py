# Generated by Django 2.2.2 on 2019-07-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_question_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='index',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
