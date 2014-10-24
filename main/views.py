__author__ = 'paulina'

from django.shortcuts import render
from django.views.generic import ListView
from .models import Photograph

def home(request):
    return render(request, 'home.html')

class PhotographIndex(ListView):
    model = Photograph