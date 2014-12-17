__author__ = 'paulina'

from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Photograph, Album, Category
from django.contrib import messages
from allauth.account.utils import get_user_model
from user_account.models import UserAccount

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

    def get_success_url(self):
        messages.success(self.request, 'Category successfully created')
        return super().get_success_url()


class CategoryShow(DetailView):
    model = Category

class CategoryUpdate(UpdateView):
    model = Category
    success_url = '/'
    fields = category_field

    def get_success_url(self):
        messages.success(self.request, 'Category successfully updated')
        return super().get_success_url()

class CategoryDelete(DeleteView):
    model = Category
    success_url = '/'

    def get_success_url(self):
        messages.success(self.request, 'Category successfully deleted')
        return super().get_success_url()



class AlbumIndex(ListView):
    model = Album

class AlbumCreate(CreateView):
    model = Album
    success_url = '/'
    fields = album_field

    def get_success_url(self):
        messages.success(self.request, 'Album successfully created')
        return super().get_success_url()

class AlbumShow(DetailView):
    model = Album

class AlbumUpdate(UpdateView):
    model = Album
    success_url = '/'
    fields = album_field

    def get_success_url(self):
        messages.success(self.request, 'Album successfully updated')
        return super().get_success_url()

class AlbumDelete(DeleteView):
    model = Album
    success_url = '/'

    def get_success_url(self):
        messages.success(self.request, 'Album successfully deleted')
        return super().get_success_url()



class PhotographIndex(ListView):
    model = Photograph

class PhotographCreate(CreateView):
    model = Photograph
    success_url = '/'
    fields = photograph_field

    def get_success_url(self):
        messages.success(self.request, 'Photo successfully created')
        return super().get_success_url()

class PhotographShow(DetailView):
    model = Photograph

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pluses'] = UserAccount.objects.filter(pluses=kwargs['object'].id).count()
        return context


class PhotographUpdate(UpdateView):
    model = Photograph
    success_url = '/'
    fields = photograph_field

    def get_success_url(self):
        messages.success(self.request, 'Photo successfully updated')
        return super().get_success_url()

class PhotographDelete(DeleteView):
    model = Photograph
    success_url = '/'

    def get_success_url(self):
        messages.success(self.request, 'Photo successfully deleted')
        return super().get_success_url()

def plusPhoto(request, photo):
    user = get_user_model()
    photo = Photograph.objects.filter(id=photo)
    user.pluses.add(photo)