from django.contrib import admin
from .models import*
from contact.forms import LocationForm 
from contact.forms import ContactForm 


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display = ('name','email','phoneno','message')

admin.site.register(Contact,ContactAdmin)

class LocationAdmin(admin.ModelAdmin):
    form = LocationForm
    list_display = ('email','phoneno','address','status','updated_by','updated_on')

admin.site.register(Location,LocationAdmin)
