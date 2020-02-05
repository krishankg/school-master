from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView
from .models import 
# Create your views here.

class PrincipalView(TemplateView):
    template_name = 'principal.html'
    modal = Message

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.modal.objects.filter(status=True).first() 
        return context
    
    def get(self,request,*args, **kwargs):
        return self.render_to_response(self.get_context_data(*args, **kwargs))

