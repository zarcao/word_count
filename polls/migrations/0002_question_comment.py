# Generated by Django 2.0.5 on 2018-05-24 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='comment',
            field=models.TextField(default='这小子什么都没留!'),
        ),
    ]
