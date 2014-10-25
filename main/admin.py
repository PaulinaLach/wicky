from django.contrib import admin
from main.models import Category, Album, Photograph, UserProfile

admin.site.register(Category)
admin.site.register(Album)
admin.site.register(Photograph)
admin.site.register(UserProfile)