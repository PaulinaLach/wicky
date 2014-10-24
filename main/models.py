from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Photograph(models.Model):
    name = models.CharField(max_length=100)
    data = models.ImageField(upload_to='images/')
    comment = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    albums = models.ManyToManyField(Album)

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])



