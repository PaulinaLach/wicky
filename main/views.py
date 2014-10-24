__author__ = 'paulina'

from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Photograph, Album, Category

category_field = ['name']
album_field = ['name', 'user']
photograph_field = ['name', 'data', 'comment', 'latitude', 'longitude', 'user', 'category', 'albums']

def home(request):
    return render(request, 'home.html')

class CategoryIndex(ListView):
    model = Category

class CategoryCreate(CreateView):
    model = Category
    success_url = '/'
    fields = category_field

class CategoryShow(DetailView):
    model = Category

class CategoryUpdate(UpdateView):
    model = Category
    success_url = '/'
    fields = category_field

class CategoryDelete(DeleteView):
    model = Category
    success_url = '/'



class AlbumIndex(ListView):
    model = Album

class AlbumCreate(CreateView):
    model = Album
    success_url = '/'
    fields = album_field

class AlbumShow(DetailView):
    model = Album

class AlbumUpdate(UpdateView):
    model = Album
    success_url = '/'
    fields = album_field

class AlbumDelete(DeleteView):
    model = Album
    success_url = '/'



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