from django.contrib import admin
from .models import News
from .forms import NewsForm

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ('title', 'content', 'status')

admin.site.register(News,NewsAdmin)