from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from Softuni_Web_Framewrok.main.models import Item


class IndexView(ListView):
    template_name = 'index.html'
    model = Item