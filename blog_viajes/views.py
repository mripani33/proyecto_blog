from re import template
from django.shortcuts import render
from django.views.generic import ListView
from .models import Entrada

from blog_viajes.models import Entrada
# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    model = Entrada
    



