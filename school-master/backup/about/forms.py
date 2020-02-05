from django import forms
from about.models import About
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)


class AboutForm(forms.ModelForm):
    
    class Meta:
        model = About
        fields = ['title','slug','content','status']