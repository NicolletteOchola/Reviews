from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer

def index(request):
  date = dt.date.today()
  projects = Projects.get_projects()
  return render(request, 'index.html', {"date": date, "projects":projects})

def register(request):
  if request.method == 'POST':
    from = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}')
      return redirect('/')
  else:
    form = RegisterForm()
  return render(request, 'registration/registration_form.html', {'form':form})

@login_required(login_url='/accounts/login/')
def search_projects(request):
  if 'keyword' in request.GET and request.GET["keyword"]:
    search_term = request.GET.get("keyword")
    searched_projects = Projects.search_projects(search_term)
    message = f"{search_term}"
    return render(request, 'search.html', {"message":message,"projects": searched_projects})

  else:
    message = "No term has been searched"
    return render(request, 'search.html', {"message": message})

def get_project(request, id):
  try:
    project = Projects.objects.get(pk = id)

  except ObjectDoesNotExist:
    raise Http404()

  return render(request, "projects.html", {"project":project})


