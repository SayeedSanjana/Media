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
    path('blog_list/',views.BlogList.as_view(),name="blog_list"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('profile/',views.userprofile,name="profile"),
    path('change_profile/',views.user_change,name="change_profile"),
    path('password/',views.pass_change,name="pass_change"), 
    path('add-picture/',views.add_pro_pic,name="add_pro_pic"), 
    path('change-picture/',views.change_pro_pic,name="change_pro_pic"),
    path('write/',views.CreateBlog.as_view(),name="create_blog") , 
    path('details/<int:id>',views.blog_details,name="blog_details"),
    path('liked/<pk>/',views.liked,name="liked_post"),
    path('unliked/<pk>/',views.unliked,name="unliked_post"),
    path('my_blogs',views.MyBlogs.as_view(),name="my_blogs"),
    path('my_blogs/<pk>/',views.UpdateBlog.as_view(),name="edit_blog"),
    

   
   
]


  