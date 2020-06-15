# Generated by Django 2.1.5 on 2020-06-14 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0013_auto_20200612_0107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.Songs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlist_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
