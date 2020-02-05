from django import forms
from contact.models import Location
from contact.models import Contact


from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name','email','phoneno','message']

class LocationForm(forms.ModelForm):
    
    class Meta:
        model = Location
        fields = ['email','phoneno','address','log','lat','status']