from django import forms
from principal.models import Message
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)


class MessageForm(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = ['title','slug','content','status']