from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from music.models import Artist,Album,Lyrics,Songs,Blog,Comment,Likes,UserInfo,User_Playlists
from django.views import generic 
from django.templatetags.static import static
from django.db import connection
from music.forms import SignUpForm,UserProfileChange,ProfilePic,CommentForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,ListView,DetailView,View,DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid


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
	return render(request,'music/first.html',context=diction1)

def base(request):
	diction2={}
	return render(request,'music/base.html',context=diction2)	

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

def lyrics(request):
	songs=Songs.objects.order_by('song_Name')
	lyrics_diction={'songs':songs}
	return render(request,'music/lyrics.html',context=lyrics_diction)





#def register(request):

	#registered=False
	#if request.method=='POST':
		#user_form=UserForm(data=request.POST)
		#user_info_form=UserInfoForm(data=request.POST)

		#if user_form.is_valid() and user_info_form.is_valid():
			#user=user_form.save()
			#user.set_password(user.password)
			#user.save()

			#user_info=user_info_form.save(commit=False)
			#user_info.user=user

			#if 'profile_pic' in request.FILES:
				#user_info.profile_pic=request.FILES['profile_pic']

			#user_info.save()
			#registered=True	
			
	#else:
		#user_form=UserForm()
		#user_info_form=UserInfoForm()
	    
	#reg_diction={'user_form':user_form,'user_info_form':user_info_form,'registered':registered,}
	#return render(request,'music/register.html',context=reg_diction)


def initial(request):
	initial_diction={}
	return render(request,'music/initial.html',context=initial_diction)


def solo_artist(request,pk):
	artist=Artist.objects.get(pk=pk)
	artist_diction={'artist':artist}
	return render(request,'music/solo_artist.html',context=artist_diction)




def register(request):
	form=SignUpForm()
	registered=False

	if request.method=='POST':
		form=SignUpForm(data=request.POST)

		if form.is_valid():
			form.save()
			registered=True

	register_dict={'form':form,'registered':registered}
	return render(request,'music/register.html',context=register_dict)		


def login_page(request):
	form=AuthenticationForm()

	if request.method=='POST':
		form=AuthenticationForm(data=request.POST)

		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username=username,password=password)

			if user is not None:
				login(request,user)
				return HttpResponseRedirect(reverse('music:mains'))
	return render(request,'music/login.html',context={'form':form})	

@login_required
def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('music:mains'))



@login_required
def userprofile(request):
	return render(request,'music/userprofile.html',context=None)	


@login_required
def user_change(request):
	current_user=request.user
	form=UserProfileChange(instance=current_user)
	if request.method=='POST':
		form=UserProfileChange(request.POST,instance=current_user)
		if form.is_valid():
			form.save()
			form=UserProfileChange(instance=current_user)
	return render(request,'music/change_profile.html',context={'form':form})		




@login_required
def pass_change(request):
	current_user=request.user
	changed=False
	form=PasswordChangeForm(current_user)
	if request.method=='POST':
		form=PasswordChangeForm(current_user,data=request.POST)
		if form.is_valid():
			form.save()
			changed=True
	return render(request,'music/pass_change.html',context={'form':form,'changed':changed})


@login_required
def add_pro_pic(request):
	form=ProfilePic()
	if request.method=='POST':
		form=ProfilePic(request.POST,request.FILES)
		if form.is_valid():
			user_obj=form.save(commit=False)
			user_obj.user=request.user
			user_obj.save()
			return HttpResponseRedirect(reverse('music:profile'))
	return render(request,'music/pro_pic_add.html',context={'form':form})

@login_required
def change_pro_pic(request):
	form=ProfilePic(instance=request.user.user_profile)
	if request.method=='POST':
		form=ProfilePic(request.POST,request.FILES,instance=request.user.user_profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('music:profile'))
	return render(request,'music/pro_pic_add.html',context={'form':form})			
    


def blog(request):
	blog_diction={}
	return render(request,'music/blog.html',context=blog_diction)


class MyBlogs(LoginRequiredMixin,TemplateView):
	template_name='music/my_blogs.html'


	

class CreateBlog(LoginRequiredMixin,CreateView):
	model=Blog
	template_name='music/create_blog.html'
	fields=('blog_title','blog_content','blog_image',)

	def form_valid(self,form):
		blog_obj=form.save(commit=False)
		blog_obj.blog_image=form.cleaned_data['blog_image']
		blog_obj.author=self.request.user
		title=blog_obj.blog_title
		blog_obj.slug=title.replace(" ","-")+"-"+str(uuid.uuid4())
		blog_obj.save()
		return HttpResponseRedirect(reverse('music:blog_list'))


class BlogList(ListView):
	context_object_name='blogs'
	model=Blog
	template_name='music/blog_list.html'
	queryset=Blog.objects.order_by('-publish_date')



@login_required
def blog_details(request,id):
	blog=Blog.objects.get(id=id)
	comment_form=CommentForm()
	already_liked=Likes.objects.filter(blog=blog,user=request.user)
	if already_liked:
		liked=True
	else:
		liked=False
	if request.method=='POST':
		comment_form=CommentForm(request.POST)
		if comment_form.is_valid:
			comment=comment_form.save(commit=False)
			comment.user=request.user
			comment.blog=blog
			comment.save()
			return HttpResponseRedirect(reverse('music:blog_details',kwargs={'id':id}))
	return render(request,'music/blog_details.html',context={'blog':blog,'comment_form':comment_form,'liked':liked})		

@login_required
def liked(request,pk):
	blog=Blog.objects.get(pk=pk)
	user=request.user
	already_liked=Likes.objects.filter(blog=blog,user=user)
	if not already_liked:
		liked_post=Likes(blog=blog,user=user)
		liked_post.save()
	return HttpResponseRedirect(reverse('music:blog_details',kwargs={'id':blog.id}))
	

@login_required
def unliked(request,pk):
	blog=Blog.objects.get(pk=pk)
	user=request.user
	already_liked=Likes.objects.filter(blog=blog,user=user)
	already_liked.delete()
	return HttpResponseRedirect(reverse('music:blog_details',kwargs={'id':blog.id}))	


class UpdateBlog(LoginRequiredMixin,UpdateView):
	model=Blog
	fields=('blog_title','blog_content','blog_image')
	template_name='music/edit_blog.html'

	def get_success_url(self,**kwargs):
		return reverse_lazy('music:blog_details',kwargs={'id':self.object.id})


@login_required
def user_playlist(request,pk):
	songs=Songs.objects.get(pk=pk)
	user=request.user
	already_in_playlist=User_Playlists.objects.filter(track=songs,user=user)
	if not already_in_playlist:
		playlist=User_Playlists(track=songs,user=user)
		playlist.save()
	return HttpResponseRedirect(reverse('music:view_playlist'))


@login_required
def view_playlist(request):
	user=request.user
	playlist=User_Playlists.objects.order_by('track').filter(user=user)
	songs=Songs.objects.filter(pk=playlist)
	palylist_diction={}
	return render(request,'music/user_playlist.html',context={'playlist':playlist,'songs':songs})









	