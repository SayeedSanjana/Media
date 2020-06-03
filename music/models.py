from django.db import models



class Artist(models.Model):

	Artist_name=models.CharField(max_length=300)
	BirthPlace=models.CharField(max_length=250,blank=True)
	Born=models.DateField(blank=True)
	Best_Songs=models.CharField(max_length=1000,blank=True)
	Best_Albums=models.CharField(max_length=1000,blank=True)
	Artist_Description=models.TextField(max_length=10000)
	Category=models.CharField(max_length=300,blank=True)
	Artist_logo=models.CharField(max_length=250,blank=True)
	
	
	def split_tags(self):
		return self.Best_Songs.split(',')
	
    	

	#def __str__(self):
	#	return self.Artist_name+""+self.Best_Albums+""+self.Best_Albums+""+self.Best_Songs


class Album	(models.Model):
	
	artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
	Album_title=models.CharField(max_length=250)
	release_date=models.DateField()
	album_logo=models.CharField(max_length=250)
	review=(
     (1,"Worst"),
     (2,"Bad"),
     (3,"Not Bad"),
     (4,"Good"),
     (5,"Very Good"),
     (6,"Excellent"),
		)
	count_reviews=models.IntegerField(choices=review)
	genre=models.CharField(max_length=100)
	is_favourite=models.BooleanField(default=False)
	Album_Description=models.TextField(max_length=10000,blank=True)

	def __str__(self):
		return self.Album_title

class Lyrics(models.Model):
	#song=models.ForeignKey(Songs,on_delete=models.CASCADE)
	lyrics=models.TextField(max_length=5000)
	lyricist=models.CharField(max_length=250)
	lyricist_descrption=models.TextField(max_length=10000,blank=True)

	def __str__(self):
		return self.lyrics



class Songs(models.Model):

	   
	song_Name=models.CharField(max_length=250)
	album=models.ForeignKey(Album,on_delete=models.CASCADE)
	artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
	lyrics=models.ForeignKey(Lyrics,on_delete=models.CASCADE)
	genre=models.CharField(max_length=100)
	length=models.CharField(max_length=500,blank=True)
	song_runtime=models.DurationField()
	song_filetype=models.CharField(max_length=100)
	audio_file = models.FileField(upload_to='audio/', blank=True)
	video_url=models.CharField(max_length=100,blank=True)
	is_favourite=models.BooleanField(default=False)
	song_description=models.CharField(max_length=500,blank=True)

	
	rating=(
      (1,"One_Star"),
      (2,"Two_Star"),
      (3,"Three_Star"),
      (4,"Four_Star"),
      (5,"Five_Star"),
		)
	song_logo=models.CharField(max_length=250)
	num_stars=models.IntegerField(choices=rating)
	Trends=models.CharField(max_length=200,blank=True)

	
















































































