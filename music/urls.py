from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from music.views import AudioListView
app_name='music'

urlpatterns = [
    
    #/music
    path('',views.mains,name='mains'),
    path('artists/',views.index,name='index'),
    path('songs/',views.song,name='song'),
    path('audios/',views.audios,name='audios'),
    path('audio/',AudioListView.as_view(), name='audio'),
    path('songs/<int:song_id>/',views.detail,name='detail'),
    path('album/',views.album,name='album'),
    path('album/<int:album_id>',views.info,name='info'),
    path('band/',views.band,name='band'),
    path('register/',views.register,name="register"),

    ]


  