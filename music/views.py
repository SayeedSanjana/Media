from django.shortcuts import render
from django.http import HttpResponse
from music.models import Artist,Album,Lyrics,Songs
from django.views import generic
from django.templatetags.static import static
from django.db import connection



# Create your views here.
class AudioListView(generic.ListView):
	context_object_name = 'audio'
	template_name ='music/audio.html'
	model =Songs

	def get_context_data(self, **kwargs):
		context = super(AudioListView, self).get_context_data(**kwargs)
		context['audio'] =Songs.objects.all()
		return context
        
        

    
def audios(request):
	diction3={}
	songs=Songs.objects.order_by('genre')
	diction3={'audios':songs,}
	return render(request,'music/audio.html',context=diction3)



def mains(request):
	diction1={}
	return render(request,'music/base.html',context=diction1)

def index(request):
	best_songs=[]
	best_albums=Artist.objects.values('Best_Albums')
	best_songs=Artist.objects.values('Best_Songs')
	artist_info=Artist.objects.order_by('Artist_name').exclude(Category="Band")
	diction={'artist_info':artist_info,'best_songs':best_songs,'best_albums':best_albums,}
	return render(request,'music/index.html',context=diction)


def song(request):
	songs=Songs.objects.order_by('genre').filter(Trends='Trending')
	songs1=Songs.objects.order_by('genre').filter(Trends='Classic')
	songs2=Songs.objects.order_by('genre').filter(Trends='Popular')
	songs3=Songs.objects.order_by('genre').filter(Trends='New')
	diction2={'songs':songs,'songs1':songs1,'songs2':songs2,'songs3':songs3}
	return render(request,'music/song.html',context=diction2)

def detail(request,song_id):

	detail=Songs.objects.get(pk=song_id)
	diction_detail={'detail':detail,}
	return render(request,'music/audio.html',context=diction_detail)

def album(request):
	album=Album.objects.order_by('Album_title')
	album_diction={'album':album,}
	return render(request,'music/album.html',context=album_diction)


def info(request,album_id):
	cursor = connection.cursor()
	cursor.execute("SELECT music_artist.Artist_name  FROM music_artist INNER JOIN music_album ON music_artist.id = music_album.artist_id  WHERE music_album.id = %s",[album_id])
	artist= cursor.fetchone()
	album=Album.objects.all()
	artist_diction={'artist':artist,'album':album}
	return render(request,'music/info.html',context=artist_diction)
	#artist=Artist.objects.raw("SELECT `music_artist.Artist_name` FROM music_artist INNER JOIN music_album ON `music_artist.id`=`music_album.artist_id` WHERE `music_album.id` = %s", [album_id])
	
	
def band(request):
	band=Artist.objects.order_by('Artist_name').filter(Category="Band")
	band_diction={'band':band}
	return render(request,'music/band.html',context=band_diction)
	


	




 	




	