from django.contrib import admin
from .models import Message
from .forms import MessageForm

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    form = MessageForm
    list_display = ('title', 'content', 'status','created_by','created_on')

admin.site.register(Message,MessageAdmin)