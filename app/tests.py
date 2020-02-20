from django.test import TestCase
from .models import *
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class UserTest(TestCase):
  def setUp(self):
    self.nicole= User(first_name = 'Nicole', last_name = 'Ochola', email = 'nicoleochola@gmail.com')
  
  def test_profile_creation(self):
    self.assertTrue(isinstance(self.nicole,User))

class ProjectsTest(TestCase):
  def setUp(self):
    self.akan= Projects(project_title='AkanNames', project_image='images/default.jpg', project_description='A website that tells you your akan name', link='https://www.github.com/NicolletteOchola/AkanNames')

  def test_project_creation(self):
    self.assertTrue(isinstance(self.akan, Projects))

class UserTest2(TestCase):
    
    def create_user(self, first_name = 'Nicole', last_name = 'Ochola', email = 'nicoleochola@gmail.com'):
      return User.objects.create(first_name =first_name, last_name =last_name, email=email)

    def test_user_creation(self):
      u = self.create_user()
      self.assertTrue(isinstance(u, User))

