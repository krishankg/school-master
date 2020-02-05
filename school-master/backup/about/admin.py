from django.contrib import admin
from .models import About
from .forms import AboutForm
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    form = AboutForm
    list_display = ('title', 'content', 'status','created_by','created_on')

admin.site.register(About,AboutAdmin)