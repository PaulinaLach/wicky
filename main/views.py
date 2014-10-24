__author__ = 'paulina'

from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Photograph

def home(request):
    return render(request, 'home.html')

class PhotographIndex(ListView):
    model = Photograph

class PhotographCreate(CreateView):
    model = Photograph
    success_url = '/'

class PhotographShow(DetailView):
    model = Photograph

class PhotographUpdate(UpdateView):
    model = Photograph
    success_url = '/'

class PhotographDelete(DeleteView):
    model = Photograph
    success_url = '/'