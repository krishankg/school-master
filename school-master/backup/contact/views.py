from django.views.generic import CreateView,TemplateView
from django.http import JsonResponse
from .models import Contact ,Location
from .forms import ContactForm


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    modal = Contact

    def post(self,request,*args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
    
    def form_valid(self, form):
        form.save()
        if self.request.is_ajax():
            data = {'success_url': reverse_lazy('contact:home'), 'error': False}
            return JsonResponse(data)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address']  = Location.objects.filter(status=True).first()
        return context
    
