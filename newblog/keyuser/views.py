from django.shortcuts import render, HttpResponse
import nacl.utils
from nacl.public import PrivateKey, Box
from django.views.generic import TemplateView, ListView

# Create your views here.
class IndexView(TemplateView):
    
    template_name = 'keyuser.html'
    def get_context_data(self, **kwargs):
        skbob = PrivateKey.generate()
        pkbob = skbob.public_key
        context = super().get_context_data(**kwargs)
        context['skkey'] = pkbob
        return context