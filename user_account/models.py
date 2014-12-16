from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Photograph
MALE = 'male'
FEMALE = 'female'
genders = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
)

class UserAccount(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(choices=genders, default=MALE, max_length=20, blank=False)
    avatar = models.ImageField(upload_to='images/avatar/', blank=True)
    about = models.TextField(blank=True)
    pluses = models.ManyToManyField(Photograph)

    REQUIRED_FIELDS = ["email"]