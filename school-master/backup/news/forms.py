from django import forms
from news.models import*
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)


class NewsForm(forms.ModelForm):
    
    class Meta:
        model = News
        fields = ['title','slug','content','status']