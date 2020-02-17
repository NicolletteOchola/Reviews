from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from PIL import image
from django_countries.fields import CountryField
from star_ratings.models import Rating

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.cascade)
  bio = models.TextField(blank=True)
  photo = models.ImageField(upload_to='profile_pics/', blank=True, default='profile_pics/default.jpg')
