from django.test import TestCase
from .models import *
from django.db import models
from django.contrib.auth.models import User

class ProfileTest(TestCase):
  def setUp(self):
    self.nicole= User(first_name = 'Nicole', last_name = 'Ochola', email = 'nicoleochola@gmail.com')
  
  def test_profile_creation(self):
    self.assertTrue(isinstance(self.nicole,User))




