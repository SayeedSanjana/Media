from django import forms
from django.contrib.auth.models import User
from music.models import UserInfo,Blog,Comment
from django.contrib.auth.forms import UserCreationForm,UserChangeForm




#class UserForm(forms.ModelForm):
#	password=forms.CharField(widget=forms.PasswordInput())
#	class Meta():
#		model=User
#		fields=('username','email','password')





#class UserInfoForm(forms.ModelForm):
#	class Meta():
#		model=UserInfo
#		fields=('facebook_id','profile_pic')


class SignUpForm(UserCreationForm):
	email=forms.EmailField(label="Email Address",required=True)
	class Meta():
		model=User
		fields=('username','email','password1','password2')


class UserProfileChange(UserChangeForm):
	class Meta():
		model=User
		fields=('username','email','first_name','last_name','password')


class ProfilePic(forms.ModelForm):
	class Meta():
		model=UserInfo
		fields=['profile_pic']




class CommentForm(forms.ModelForm):
	class Meta():
		model=Comment
		fields=('comment',)