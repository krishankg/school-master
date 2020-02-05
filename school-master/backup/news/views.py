from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView
from .models import News
# Create your views here.

class NewsView(TemplateView):
    template_name = 'news.html'
    modal = News

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.modal.objects.all() 
        return context
    
    def get(self,request,*args, **kwargs):
        return self.render_to_response(self.get_context_data(*args, **kwargs))

