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
    path('blog/',views.blog,name="blog"),
    path('initial/',views.initial,name="initial"),
    path('blog/blog_list/',views.blog_list,name="blog_list"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('profile/',views.userprofile,name="profile"),
    path('change_profile/',views.user_change,name="change_profile"),
    path('password/',views.pass_change,name="pass_change"), 
    path('add-picture/',views.add_pro_pic,name="add_pro_pic"), 
    path('change-picture/',views.change_pro_pic,name="change_pro_pic"),    
   


    ]


  