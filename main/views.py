__author__ = 'paulina'

from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Photograph

photograph_field = ['name', 'data', 'comment', 'latitude', 'longitude', 'user', 'category', 'albums']

def home(request):
    return render(request, 'home.html')

class PhotographIndex(ListView):
    model = Photograph

class PhotographCreate(CreateView):
    model = Photograph
    success_url = '/'
    fields = photograph_field

class PhotographShow(DetailView):
    model = Photograph

class PhotographUpdate(UpdateView):
    model = Photograph
    success_url = '/'
    fields = photograph_field

class PhotographDelete(DeleteView):
    model = Photograph
    success_url = '/'