from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from posts.models import Post
from django import forms
from django.db import models
from django.forms import ModelForm

User = get_user_model()


#  создадим собственный класс для формы регистрации
#  сделаем его наследником предустановленного класса UserCreationForm
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ("first_name", "last_name", "username","desc", "email","image")
        
        def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          #for field in self.fields:
            #self.fields[field].widget.attrs['autocomplete'] = 'off'
          self.fields['first_name'].widget.attrs['placeholder'] = 'Your first name'
          self.fields['last_name'].widget.attrs['placeholder'] = 'Your last name'
          self.fields['username'].widget.attrs['placeholder'] = 'Your username'
          self.fields['email'].widget.attrs['placeholder'] = 'Your email'
          self.fields['desc'].widget.attrs['placeholder'] = 'Status'

class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','text','image')
        def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in self.fields:
            self.fields[field].widget.attrs['autocomplete'] = 'off'
            self.fields['title'].widget.attrs['placeholder'] = 'Title'
            self.fields['text'].widget.attrs['placeholder'] = 'Post'