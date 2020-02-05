from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView
from .models import About
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'
    modal = About

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.modal.objects.filter(status=True).first() 
        return context
    
    def get(self,request,*args, **kwargs):
        return self.render_to_response(self.get_context_data(*args, **kwargs))

