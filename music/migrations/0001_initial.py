# Generated by Django 2.1.5 on 2020-05-20 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album_title', models.CharField(max_length=250)),
                ('release_date', models.DateField()),
                ('album_logo', models.CharField(max_length=250)),
                ('count_reviews', models.IntegerField(choices=[(1, 'Worst'), (2, 'Bad'), (3, 'Not Bad'), (4, 'Good'), (5, 'Very Good'), (6, 'Excellent')])),
                ('genre', models.CharField(max_length=100)),
                ('is_favourite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Artist_name', models.CharField(max_length=300)),
                ('BirthPlace', models.CharField(blank=True, max_length=250)),
                ('Born', models.DateField(blank=True)),
                ('Best_Songs', models.CharField(blank=True, max_length=1000)),
                ('Best_Albums', models.CharField(blank=True, max_length=1000)),
                ('Artist_Description', models.CharField(max_length=3000)),
                ('Category', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Lyrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyrics', models.TextField(max_length=5000)),
                ('lyricist', models.CharField(max_length=250)),
                ('lyricist_descrption', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_Name', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=100)),
                ('length', models.CharField(blank=True, max_length=500)),
                ('song_runtime', models.DurationField()),
                ('song_filetype', models.CharField(max_length=100)),
                ('audio_file', models.FileField(blank=True, upload_to='audio/')),
                ('video_url', models.CharField(blank=True, max_length=100)),
                ('is_favourite', models.BooleanField(default=False)),
                ('song_description', models.CharField(blank=True, max_length=500)),
                ('song_logo', models.CharField(max_length=250)),
                ('num_stars', models.IntegerField(choices=[(1, 'One_Star'), (2, 'Two_Star'), (3, 'Three_Star'), (4, 'Four_Star'), (5, 'Five_Star')])),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Artist')),
                ('lyrics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Lyrics')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Artist'),
        ),
    ]
