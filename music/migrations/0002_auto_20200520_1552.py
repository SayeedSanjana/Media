# Generated by Django 2.1.5 on 2020-05-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='Artist_Description',
            field=models.CharField(max_length=10000),
        ),
    ]
