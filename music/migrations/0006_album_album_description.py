# Generated by Django 2.1.5 on 2020-05-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20200522_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='Album_Description',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
