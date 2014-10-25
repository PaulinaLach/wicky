from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

class Photograph(models.Model):
    name = models.CharField(max_length=100)
    data = models.ImageField(upload_to='images/photos/')
    comment = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ForeignKey(Category)
    albums = models.ManyToManyField(Album)

    def __str__(self):
        return self.name

    class Meta:
        get_latest_by = 'creation_date'