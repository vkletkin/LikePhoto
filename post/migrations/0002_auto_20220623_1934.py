# Generated by Django 2.2 on 2022-06-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
